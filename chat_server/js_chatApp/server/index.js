const express = require('express');
const socketio = require('socket.io');
const http = require('http');
const {removeUser,
    getUser,
    getUsersInRoom,
    isOtpValid, 
    generateKey,
    initiateUser, 
    getNewUser, 
    generateId, 
    MasterUser, 
    addLiveUser,
     getLiveUser,
    UpdateUserBackend,
    sendMessage} = require('./users.js');
const PORT = process.env.PORT || 5000;
const router = require('./router');
const app = express();
const server = http.createServer(app);
const path = require('path');


const io=socketio(server,{
    cors: {
        origin: process.env.CHAT_SERVER || '*' ,
        credentials: true
      }
});

io.on('connection',(socket)=>
{
    console.log("We have a new connection");
    const id = socket.handshake.query.id;
    const verificationId = socket.handshake.query.verificationId;
    const token = socket.handshake.query.token;
    io.to(MasterUser().id).emit('roomData',{users:getUsersInRoom()});
    if (getUser(id))
    {
    const user=getUser(id);
    if (user.token == token) {
            if (!getLiveUser(user.id)){
                addLiveUser(user);
                socket.broadcast.to(MasterUser().id).emit('message',{sender:id, name:`${user.name}`, text: `${user.name}, has joined!`});
            }
            socket.emit('message',{sender:MasterUser().id, name: MasterUser().name, text:`${user.name}, welcome to the chat`});
            io.to(MasterUser().id).emit('roomData',{users:getUsersInRoom()});
            socket.join(id);

            socket.on('sendMessage', (message,callback)=>{
                let state=false;
                const user=getUser(socket.handshake.query.id);
                if (user) {
                    state=true;
                    //console.log('message',{recipient:message.recipient,sender:message.sender, name:user.name,text:message.text});
                    sendMessage({sender:user.id,
                                recipient:message.recipient,
                                senderName:user.name,
                                text:message.text});
                    io.to(message.recipient).emit('message',{sender:message.sender, name:user.name,text:message.text});
                    callback();
                    //callback(state);
                }else{
                //callback(state);
                    };
            
            })
            socket.on('disarm',()=>{
                console.log("user has disconnected");
                let user;
                if (socket.handshake.query.id != MasterUser().id) {
                user= removeUser(socket.handshake.query.id);
                }
                if (user)
                {
                io.to(MasterUser().id).emit('message', {sender:socket.handshake.query.id, text:`${user.name} has left`});
                io.to(MasterUser().id).emit('roomData',{room:user.room,users:getUsersInRoom(user.room)});
                }
            });
    }}
    socket.on('initiateUser',({mobile, verificationId},callback)=>{
        const id = generateId();
        const key=generateKey({mobile});
        initiateUser({id:id,mobile:mobile,
                token:key, verificationId:verificationId
        });
    });
    socket.on('otp',({name,mobile,otp,verificationId},callback)=>{
        const user = getNewUser({mobile});
        if (user) {
            (async()=>{
                const credential = await isOtpValid(user,otp,verificationId);
                    if (credential) {
                        if(user.name!=MasterUser().name){user.name=name};
                        user.gcredential=credential;
                        socket.emit('getToken',{id:user.id,name:user.name,token:user.token,mobile:user.mobile,gcredential:credential});
                        console.log('token sent');
                        UpdateUserBackend(user);
                        }else {
                            callback('', "otp didn't match , retry and login");
                        }
                
            })().catch(error=>console.log(error));
        }else {
            callback('',"user with mobile not found, relogin");
        }

    });
    socket.on('disconnect', ()=>{
                                  const id = socket.handshake.query.id;
                                  console.log(`disconnected id:${id}`);
                                  if(getLiveUser(id)){
                                    removeUser(id); 
                                    io.to(MasterUser().id).emit('roomData',{users:getUsersInRoom()});
                                  }
                                })
      
});

app.use(express.static(path.join(__dirname, 'build')));
app.use(router);
server.listen(PORT, () => console.log(`Server has started on port ${PORT}`));

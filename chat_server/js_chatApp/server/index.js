const express = require('express');
const socketio = require('socket.io');
const http = require('http');
const { addUser,removeUser,getUser,getUsersInRoom} = require('./users.js');
const PORT = process.env.PORT || 5000;
const router = require('./router');
const app = express();
const server = http.createServer(app);
const path = require('path');
const io=socketio(server,{
    cors: {
        origin: "http://localhost:3000",
        credentials: true
      }
});

io.on('connection',(socket)=>
{
    console.log("We have a new connection");
    let error,user;
    socket.on('join',({name,room},callback)=>{
        if (!name || !room) {
            {error:'UserName is taken'}
        }else {
        let {error,user} = addUser({id:socket.id,name,room});
        if (error) {return callback(error)};
        socket.emit('message',{user:'admin',text:`${user.name}, welcome to the room ${user.room}` });
        socket.broadcast.to(user.room).emit('message',{user:'admin', text: `${user.name}, has joined!`});
        socket.join(user.room);
        io.to(user.room).emit('roomData',{room:user.room,users:getUsersInRoom(user.room)});
        };

        if (error) {return callback(error)};
  
        
    });
    socket.on('sendMessage', (message,callback)=>{
        let state=false;
        const user=getUser(socket.id);
        if (user) {
            state=true;
            io.to(user.room).emit('message',{user:user.name, text:message});
            callback(state);
        }else{
        callback(state);};
    
    })
    socket.on('disconnect',()=>{
        console.log("user has disconnected")
        const user= removeUser(socket.id);

        if (user)
        {
           io.to(user.room).emit('message', {user:'admin', text:`${user.name} has left`});
           io.to(user.room).emit('roomData',{room:user.room,users:getUsersInRoom(user.room)});
        }
    });  
});

app.use(express.static(path.join(__dirname, 'build')));
app.use(router);

server.listen(PORT, () => console.log(`Server has started on port ${PORT}`));
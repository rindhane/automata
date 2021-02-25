import React, {useState, useEffect} from 'react';
import queryString from "query-string";
import io from "socket.io-client";
import InfoBar from '../InfoBar/InfoBar';
import  './Chat.css';
import Input from '../Input/Input';
import Messages from '../Messages/Messages';
import UserSideBar from '../UserSideBar/UserSideBar';
let socket;

const Chat = ({location})=> {
    const ENDPOINT = 'http://localhost:5000';
    const [name,setName]=useState('');
    const [room,setRoom]=useState('');
    const[roomUsers,setRoomUsers]=useState([]);
    const [message,setMessage]=useState('');
    const [messages,setMessages]=useState([]);
    useEffect(()=>{
        const {name, room}=queryString.parse(location.search);
        socket=io(ENDPOINT);
        setName(name);
        setRoom(room);
        socket.emit('join',{name: name, room:room},(error) => {
            alert(error);
        });

        return () => {
            socket.emit("disconnect");
            socket.off();
        }
    },[ENDPOINT,location.search]);

    useEffect(()=>{
        socket.on('message',(message)=> {
            setMessages([...messages, message]);
        })
    },[messages]);

    const sendMessage = (event) => {
        event.preventDefault();

        if(message) {
            socket.emit('sendMessage', message, (state)=> {
                if(state){
                setMessage("")
                }else{
                    alert('Rejoin, the connection has disrupted');
                };
                        }
                );
        }
    }

    useEffect(()=>
    {
        socket.on('roomData',({users}) => 
            {console.log("received",users);
            setRoomUsers(users.map((user)=>{return user.name}));} , [roomUsers] );
    })

    return (
        <div className="outerContainer">
            <div className="sideContainer">
               <UserSideBar users={roomUsers}/>
            </div>
            <div className="container">
                <InfoBar room={room} />
                <Messages messages={messages} name={name}/>
                <Input message={message} 
                    setMessage={setMessage}
                    sendMessage={sendMessage} 
                />
            </div>
        </div>
    )
};

export default Chat;
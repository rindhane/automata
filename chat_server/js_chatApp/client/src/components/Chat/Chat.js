import React,{useMemo, useEffect, } from 'react';
import InfoBar from '../InfoBar/InfoBar';
import  './Chat.css';
import Input from '../Input/Input';
import Messages from '../Messages/Messages';
import UserSideBar from '../UserSideBar/UserSideBar';
import { MessagesProvider } from '../../context/MessageProvider';
import { useSocket } from '../../context/socketProvider';


const Chat = ({mId, setMid})=> {
    const {SocketRelay}=useSocket();
    const Csocket=useMemo(()=>{
        return SocketRelay(mId)
    },[mId])
    useEffect(()=>{
        
        console.log('chat loaded');
        return ()=>{
            Csocket.emit('disarm');
            Csocket.close();
            }
    },[mId])
    return (
        <div className="outerContainer">
            <MessagesProvider socket={Csocket}>
                <div className="sideContainer">
                <UserSideBar socket={Csocket}/>
                </div>
                <div className="container">
                    <InfoBar  socket={Csocket} setMid={setMid}/>
                    <Messages myId={mId}/>
                    <Input  myId={mId}/>
                </div>
            </MessagesProvider>
        </div>
    )
};

export default Chat;
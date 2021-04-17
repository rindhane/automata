import React, {useContext, useEffect, useState} from 'react';
import io from "socket.io-client";


const SocketContext = React.createContext()

export function useSocket() {
    return useContext(SocketContext);
}


export function SocketProvider({mId,children}){
    const [socket,setSocket]=useState();
    const SERVER = process.env.REACT_APP_CHAT_SERVER ; 
    let name, id, token, code, mobile ;
    /*useEffect(()=>{
        if(mId) {
            ({name, id, token, code, mobile} = {mId});
            }
        const newSocket=io(SERVER,{query: {name, id,token, code, mobile}} )
        setSocket(newSocket);
        return () => {newSocket.emit('disarm');
                        newSocket.close();}
    },[mId])*/

    function SocketWorker (){
        const newSocket=io(SERVER)
            return newSocket;
                        }
    function SocketRelay (mId){
        const {name, id, token, code, mobile} = mId;                
        const newSocket=io(SERVER,{query: {name, id,token, code, mobile}});
            return newSocket;
    }

    return (
        <SocketContext.Provider value={{socket,SocketWorker,SocketRelay}}>
            {children}
        </SocketContext.Provider>
    )
}
import React, {useState,useEffect} from 'react';
import './UserSideBar.css';
import {useMessages} from '../../context/MessageProvider';
import ScrollToBottom from 'react-scroll-to-bottom';

const UserSideBar = ({socket})=> {
    const [liveUsers,setLiveUsers]=useState([]);
    const {receipientSelectedArray, selected, setSelected,messages, getNameRecipient} = useMessages();
    const {recipients:users, selectName} = receipientSelectedArray(messages,selected);
    
    useEffect(()=>{
        socket.on('roomData',({users})=>{
            setLiveUsers(users);
            console.log(users,"liveusers");
        },[liveUsers]);
        return ()=>{socket.off('roomData')};
        },[liveUsers]);
    
    const handleSelect =(e)=>{
        setSelected(e);
    }
    const checkLive = (user,someArray)=>{
        if (someArray.indexOf(user)==-1) 
        {return false}else {return true}                
    };

    return (
        <div >
            <div className="topBar">
                <h3 style={{ textAlign: 'center' }}> Users Logged In</h3>
            </div>
            <div className="userContainer">
            <ScrollToBottom>
                <ul className="flexing">
                    {users.map((user,i)=>{
                        return (
                            <div className={i==selected ? 'active' : ''}>
                            <li action style={checkLive(user,liveUsers)? null : {color:'red'}} onClick={()=>{handleSelect(i)}}  key={i}>{getNameRecipient(messages,user)}</li>
                            </div>
                            );
                    })
                    }
                </ul>
            </ScrollToBottom>
            </div>
        </div>
    );
    
};

export default UserSideBar;
import React,{useState,useEffect} from 'react';
import { useMessages } from '../../context/MessageProvider';
//import useLocalStorage from '../../hooks/useLocalStorage';
import closeIcon from '../../icons/closeIcon.png';
import onlineIcon from '../../icons/onlineIcon.png';
import './InfoBar.css';


const InfoBar=({socket,setMid}) => {
    const {receipientSelectedArray, selected, setSelected,messages} = useMessages();
    const [room,setRoom]=useState('');
    function Logout (){
        setMid();
        socket.emit('disarm')
        socket.close();
    }

    useEffect(()=>{
        const {selectName} = receipientSelectedArray(messages,selected);
        setRoom(selectName);
    },[selected,messages])
    return (
    <div className="infoBar">
        <div className="leftInnerContainer">
            <img className="onlineIcon" src={onlineIcon} alt="online image"/>
            <h3>{room}</h3>
        </div>
        <div className="rightInnerContainer">
                <a href="/" onClick={Logout}><img src={closeIcon} alt="close image" /></a>
        </div>
    </div>
    )
}

export default InfoBar; 
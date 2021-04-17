import React, {useState, useEffect} from 'react';
import './Input.css';
import {useMessages} from '../../context/MessageProvider';

const Input = ({myId}) => {
    const [message,setMessage]=useState('');
    const {receipientSelectedArray, selected,messages,sendMessage} = useMessages();
    const [room,setRoom]=useState('');
    const [nameRecipient,setnameRecipient]=useState('');

    useEffect(()=>{
        const {recipient:room,selectName} = receipientSelectedArray(messages,selected);
        setRoom(room);
        setnameRecipient(selectName);
    },  [messages,selected])


    const transferMessage = (message,room,nameRecipient) => {
        const {name,id} = myId;
        sendMessage(message,room,id, name, nameRecipient);
        setMessage('');
    }

    const handleForm=(e)=>{
        e.preventDefault();
    }
/*onKeyPress= {(event) =>{return event.key ==='Enter' ? transferMessage(message,room) : null}}}
*/

return (
    <form className="form" onSubmit={handleForm}>
        <input 
        className="input"
        type="text"
        placeholder="Type a Message...." 
        value={message}
        onChange={event=> {setMessage(event.target.value)}}
        
        />
        <button className="sendButton" 
             onClick={(event) => {
                event.preventDefault();
                transferMessage(message,room,nameRecipient);
             }}>Send</button>
    </form>
)
}

export default Input;
import React , {useState,useEffect} from 'react';
import './Messages.css';
import Message from './Message/Message';
import ScrollToBottom from 'react-scroll-to-bottom';
import {useMessages} from '../../context/MessageProvider';


const Messages = ({myId}) => {

    const [conversations,setConversations]=useState([]);
    const [room,setRoom]=useState('');
    const { formattedMessages, receipientSelectedArray,selected, messages} = useMessages();
    
    useEffect(()=>{
        const {recipient}=receipientSelectedArray(messages,selected);
        setConversations(formattedMessages(recipient));
        setRoom(recipient);
    },[selected,messages])
    
    return (
        <ScrollToBottom className="messages">
            {
                conversations.map(
                    (message,i) => { 
                        return (
                            <div key={i}> 
                                <Message message={message} name={myId.id.toString()}/>
                            </div> ) 
                        })
            }
        </ScrollToBottom>
    );
}

export default Messages;
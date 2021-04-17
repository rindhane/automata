import React,{useContext,useState,useEffect} from 'react';
import useLocalStorage from '../hooks/useLocalStorage';

const MessagesContext = React.createContext();

export function useMessages() {
    return useContext(MessagesContext);
}

export function MessagesProvider({socket,children}){

    const [messages, setMessages] = useLocalStorage('messages',[]);
    const [selected, setSelected]=useState(0);
 

    function createMessages({recipient,conversation}) {
        setMessages(prevMessages=>{
            return [...prevMessages, {recipient, conversation} ];
        })
    }

    function sendMessage (message,room,id,name,nameRecipient) {
        if (message && room){
            const update = ()=>{

                const innerMessage = 
                            {
                                recipient:{room:room, name:nameRecipient},
                                conversation:{ senderID: id,name:name ,text:message}
                            };
                createMessages(innerMessage);
            };
            socket.emit('sendMessage',{recipient:room,
                                        sender:id,
                                        text:message},update);
            console.log('message request sent'); 
        }
    }
    useEffect(()=>{
        if(socket) {
            socket.on('message',({sender,text,name})=>{
                const innerMessage = {
                    recipient:{room:sender,name:name},
                    conversation:{senderID:sender,name:name,text:text}
                }
                createMessages(innerMessage);
            })
        }else {return };
        return ()=> socket.off('message');
    },[socket,messages]);
    
    function getNameRecipient (messages,recipient) {

        const getName = (arr,value)=>
        {
            if (value.recipient.room==recipient) 
            {
            if (arr.includes(value.recipient.name)){return arr};
            arr.push(value.recipient.name);
            return arr;
            } 
            return arr;
        }
        return messages.reduceRight(getName,[])[0];
    }


    function receipientSelectedArray(messages,selected) {
        function onlyUnique(value, index, self) {
            return self.indexOf(value) === index;
          }
        let recipients = messages.map(message => {
            return message.recipient.room
        });
        recipients=recipients.filter(onlyUnique);
        const recipient= recipients[selected];
        const selectName = getNameRecipient(messages,recipient);        
        return {recipients, recipient, selectName};
    }


    function formattedMessages(room) {
        const conversations= messages.filter(message=>{
            return message.recipient.room==room;}).map(message=>(message.conversation))
        return conversations;
    } 

    const value = {
        messages,   
        createMessages,
        sendMessage,
        formattedMessages,
        receipientSelectedArray,
        selected,
        setSelected,
        getNameRecipient,
    }

    return (
        <MessagesContext.Provider value={value}>
            {children}
        </MessagesContext.Provider>
    )

}
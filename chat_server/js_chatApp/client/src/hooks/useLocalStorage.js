import {useEffect,useState} from 'react' ;

const PREFIX='chat-client-';

export default function useLocalStorage (key,initialValue){
    const validateKey = PREFIX + key;
    const [value,setValue] = useState(() =>{
        const jsonValue=localStorage.getItem(validateKey);
        if (jsonValue !=null && jsonValue !=undefined && jsonValue!='undefined') {return JSON.parse(jsonValue)}
        if (typeof initialValue === 'function') {
            return initialValue();
        }else {
            return initialValue;
        }
    })

    useEffect(() => {
        localStorage.setItem(validateKey, JSON.stringify(value));
    },[validateKey,value])

    return [value,setValue];
}
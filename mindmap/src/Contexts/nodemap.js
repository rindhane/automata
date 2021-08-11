import React, { useState, useEffect, useContext } from 'react';

let NodeMapContext = React.createContext();

export const useNodeMapContext = ()=>{
    return useContext(NodeMapContext);
}

function getSavedValue(key,default_value) {
    const tmp = JSON.parse(localStorage.getItem(key));
    if (tmp) return tmp;   
    if (default_value instanceof Function) return default_value();
    return default_value;
}

export const node_generator = ({title,level})=> {
    return {
        title:title,
        level:level,
    }
}

const initial_generator = () =>{
    const result=[]
    for (let i=0; i<2; i++) {
        let tmp=node_generator({
            title:`Title:${i}`,
            level:i,
        })
        result.push(tmp);
    }
    return result;
}

export function NodeMapProvider({children}) {
   const [key,setKey] = useState('mainKey');
   const [ map, setMap ]= useState(()=>{
       return getSavedValue(key,initial_generator);
   });
   
   useEffect(()=>{
       localStorage.setItem(key,JSON.stringify(map));
   },[key,map])

   const nodeAdder = (newVal) =>{
    setMap([...map,newVal]);
    }   

    const ContextValues = {
        map,
        setKey,
        setMap,
        nodeAdder,
    }
   return (
       <NodeMapContext.Provider value = {ContextValues}>
           {children}
       </NodeMapContext.Provider>
   )
}
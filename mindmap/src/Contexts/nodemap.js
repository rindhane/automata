import React, { useState, useEffect, useContext } from 'react';
import {v4 as uuid} from 'uuid';

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

const initial_generator = (func) =>{
    const result=[]
    let parentId;
    for (let i=0; i<2; i++) {
        let tmp=func({
            title:`Title:${i}`,
            level:i,
            parentId: parentId ? parentId : null, 
                })
        parentId=tmp.id;
        result.push(tmp);
    }
    return result;
}

export function NodeMapProvider({children}) {
    const MAIN_KEY='mainKey';
    const node_generator = ({title,level,top,left,size,message,parentId},)=> {
            return {
            title:title,
            id:(()=>uuid())(),
            level:level ? level:1,
            top:top? top:0,
            left:left?left:0,
            size:size,
            message:message,
            parentId:parentId,
                    }
    }
   const [ map, setMap ]= useState(()=>{
       return getSavedValue(MAIN_KEY,()=>initial_generator(node_generator));
   });   
   useEffect(()=>{
       localStorage.setItem(MAIN_KEY,JSON.stringify(map));
   },[MAIN_KEY,map]);

   const nodeAdder = (newVal) =>{
    setMap([...map,newVal]);
    }
    const getNode= (id) => {
        const index= map.findIndex(element=>id===element.id);
        return map[index];
    }
    const nodeUpdater=(nodeNew)=>{
        const index=map.findIndex(element=>nodeNew.id===element.id);
        map[index]=nodeNew;
        setMap(map);
        localStorage.setItem(MAIN_KEY,JSON.stringify(map));
    }
    const ContextValues = {
        map,
        setMap,
        nodeAdder,
        node_generator,
        nodeUpdater,
        getNode,
    }
   return (
       <NodeMapContext.Provider value = {ContextValues}>
           {children}
       </NodeMapContext.Provider>
   )
}
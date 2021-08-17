import React, {useState,useEffect,useRef} from 'react';
import Node from '../node/node';
import {useNodeMapContext} from '../../Contexts/nodemap';
import './playground.css';
import {NodeConnector} from '../nodeConnector/nodeConnector';

const useRefManager = () =>{
    const [connectors,setConnectors] = useState(new Map());
    const changeRef = useRef([0,0]);
    const storeRef = (id,ref)=>{
        setConnectors(()=>{
            connectors.set(id,ref);
            changeRef.current=averageMaker(connectors);
            return connectors;
        });
    }
    const retrieveRef = (id)=> {
        return connectors.get(id)
    }

    const refLinker = ({node,id})=>{
        storeRef(id,node.getBoundingClientRect());
    }
    const averageMaker = (conMap) =>{
        let top=0;
        let left=0;
        let count=0;
        //eslint-disable-next-line
        for (let [index,rect] of conMap) {
            top=top+rect.top;
            left=left+rect.left;
            count++;
        }
        if (count){
            return [top/count,left/count];
        }
        return [top,left];
    }
 
    return {retrieveRef,refLinker,connectors,changeRef}
}

const create_node = ({index,element,size,refLinker})=>{
    element.size=element.size ? element.size:size;
    return (<Node refLinker={refLinker} key={index} element={element}/>)
}

const create_connector= (element,parent,key)=>{
    return  (<NodeConnector key={key}  element={element} parent={parent} />) 

}

const LayoutCreator = (node_map,refLinker) => {
    const ELEMENT_SIZE=50;
    return node_map.map((element,index)=>{
        return create_node({element,index,size:ELEMENT_SIZE,refLinker});
                     });
}

const Playground = () => {
    const {map,getNode} = useNodeMapContext();
    const {connectors,refLinker,changeRef}=useRefManager();
    const [connectorBox,setconnectorBox]=useState([]);
    useEffect(()=>{
        let i=0;
        const tmp=[];
        for (let conn of connectors)
        {
            const elementId=conn[0]
            const elementBox=conn[1]
            const parentId = getNode(elementId).parentId;
            const parentBox=connectors.get(parentId);
            if(parentBox && elementBox){
                tmp.push(create_connector(elementBox,parentBox,i))
            }
            i++;
        }
        setconnectorBox(tmp);
        // eslint-disable-next-line
    },[connectors,changeRef]);
    return (
        <div key={changeRef} className='canvas'>
            {LayoutCreator(map,refLinker)}
            {connectorBox}
            {(()=>{console.log('run')})()}       
        </div>
    )
}

export default Playground;
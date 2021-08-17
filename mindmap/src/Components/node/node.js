import React, { useState } from 'react';
import './node.css';
import {ReactComponent as AddSVG} from './add.svg';
import {useNodeMapContext, } from '../../Contexts/nodemap';


const onMouseMove= (e,change,top,left,
                    setLeft,setTop,element,elementUpdater) => {
    if (change){
        const topNew=top+e.movementY;
        const leftNew=left+e.movementX;
        setTop(topNew);
        setLeft(leftNew);
        element.top=topNew;
        element.left=leftNew;
        elementUpdater(element);
        };    
  }

const onMouseDown= (e, setChange, ) => {
    setChange(true);
}

const onMouseUp = (e, setChange,)=>{
    setChange(false);
}

const parsePixel=(size)=>{
    return size.toString()+'px'
}
const addNode = ({level, top, left,size,id},adder,generator)=>{
    level = level + 1; 
    top =  top + 20;
    left= left+20;
    const title='New ChildNode';
    const message= 'No Message';
    const newNode= generator({title,level,top,left,message,size,parentId:id});
    adder(newNode);
}

const Node= (props)=> {
    const element=props.element;
    const ref=props.refLinker;
    const [change,setChange]=useState(false);
    const [top,setTop]=useState(parseInt(element.top));
    const [left,setLeft]=useState(()=>{
            if (element.left) {return parseInt(element.left);}
            return 20;});
    const {nodeAdder,node_generator,nodeUpdater}=useNodeMapContext();
    let style= {height:parsePixel(element.size),
                width:parsePixel(element.size),
                top:parsePixel(top),
                left:parsePixel(left),
                };
    return (
        <div ref = {(node)=>{
            if(node)
            {ref({id:element.id,node});}
        }} className='node' 
            style = {style}
            onMouseMove={(e)=>onMouseMove(e,
                                            change,top,left,
                                            setLeft,setTop,
                                            element,nodeUpdater)}
            onMouseDown={(e)=>onMouseDown(e,setChange)}
            onMouseUp={(e)=>onMouseUp(e,setChange)}
            onMouseLeave={(e)=>onMouseUp(e,setChange)}
            onClick={(e)=>null} >
            <div className='title'>
                {element.title}
            </div>
            <div onClick = {(e)=>{
                e.preventDefault();
                addNode(element,nodeAdder,node_generator)}}> 
                <AddSVG /> 
            </div>
            <div className = 'message'>
                {element.message}
            </div>
        </div>
    )
}

export default Node;

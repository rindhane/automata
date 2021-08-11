import React, { useState } from 'react';
import './node.css';
import {ReactComponent as AddSVG} from './add.svg';
import {useNodeMapContext, node_generator} from '../../Contexts/nodemap';

const onMouseMove= (e,change,top,left,
                    setLeft,setTop,) => {
    if (change){
        setTop(top+e.movementY);
        setLeft(left+e.movementX);
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

const addNode = (title,level,func)=>{
    const newNode= node_generator ({title,level});
    console.log(newNode);
    func(newNode);


}

function Node (props) {
    const [change,setChange]=useState(false);
    const [top,setTop]=useState(parseInt(props.top));
    const [left,setLeft]=useState(0);
    //eslint-disable-next-line
    const {map,nodeAdder}=useNodeMapContext();
    // eslint-disable-next-line
    const [height,setHeight]=useState(parsePixel(props.size));
    let title=props.title;
    let message= props.message;
    let level=props.level;
    let style= {height:height,
                width:height,
                top:parsePixel(top),
                left:parsePixel(left),
                };
    return (
        <div className='node' 
            style = {style}
            onMouseMove={(e)=>onMouseMove(e,
                                            change,top,left,
                                            setLeft,setTop)}
            onMouseDown={(e)=>onMouseDown(e,setChange)}
            onMouseUp={(e)=>onMouseUp(e,setChange)}
            onMouseLeave={(e)=>onMouseUp(e,setChange)}
            onClick={(e)=>null} >
            <div className='title'>
                {title}
            </div>
            <div onClick = {(e)=>{addNode('ChildNode',level+1,nodeAdder)}}> 
                <AddSVG /> 
            </div>
            <div className = 'message'>
                {message}
            </div>
        </div>
    )
}

export default Node;

import React, { useState } from 'react';
import './node.css';

let onMouseMove= (e,change,top,left,
                    setLeft,setTop, index) => {
    if (change){
        setTop(top+e.movementY);
        setLeft(left+e.movementX);
            };    
  }

let onMouseDown= (e, setChange, index) => {
    setChange(true);
}

let onMouseUp = (e, setChange,index)=>{
    setChange(false);
}

let click=(setHeight)=>{
    setHeight('10vh');
}

function Node (props) {
    const [change,setChange]=useState(false);
    const [top,setTop]=useState(parseInt(props.top));
    const [left,setLeft]=useState(0);
    const [height,setHeight]=useState('2vh');
    let title=props.title;
    let message= props.message;
    let index=props.index;
    let style= {height:height,
                width:height,
                top:top.toString()+'px',
                left:left.toString()+'px',
                };
    return (
        <div className='node' 
            style = {style}
            onMouseMove={(e)=>onMouseMove(e,
                                            change,top,left,
                                            setLeft,setTop, index)}
            onMouseDown={(e)=>onMouseDown(e,setChange,index)}
            onMouseUp={(e)=>onMouseUp(e,setChange,index)}
            onMouseLeave={(e)=>onMouseUp(e,setChange,index)}
            onClick={(e)=>click(setHeight)} >
            <div className='title'>
                {title} {index}
            </div>
            <div className = 'message'>
                {message}
            </div>
        </div>
    )
}

export default Node;
import {useRef} from 'react';

export const NodeConnector = (props)=>{
    const element=props.element;
    const parent=props.parent;
    const buffer=20;
    const connectorRef=useRef(null);
    const svgHeight=Math.abs(parent.top-element.top)+buffer;
    const svgWidth=Math.abs(parent.left-element.left)+buffer;
    const startY = parent.height/2 ;
    const startX = parent.width;
    //assumption: element is always left of the parent
    const originX = parent.left;
    const originY = parent.top;
    const endX = element.left -originX - startX;
    const endY= element.top-originY-startY+element.height/2;
    
    const style = {
        position:'fixed',
        //borderStyle:'dotted',
        top:`${originY}px`,
        left:`${originX}px`,
        zIndex:'-1',
        };  
    return (
        <div style={style} >
            <svg ref={connectorRef} xmlns="http://www.w3.org/2000/svg"
            height={`${svgHeight}`} 
            width={`${svgWidth}px`}
            enableBackground={`new 0 0 ${svgWidth} ${svgHeight}`}
            viewBox={`0 0 ${svgWidth} ${svgHeight}` }
            fill="#000000"
            >
                <path id='connector' d={`M ${startX} ${startY} l${endX} ${endY}`} stroke="blue" strokeWidth="5" fill="none" />
            </svg>
        </div>
    );
};

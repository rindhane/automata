
import Node from '../node/node';
import {useNodeMapContext} from '../../Contexts/nodemap';

const create_node = (title,level,index,top)=>{
    return (<Node key={index} title={title} 
                level={level} 
                top={top.toString()}
                message={`message is ${index}`}
                size={50}/>)
}

const create_layout = (node_map) => {
    return node_map.map((element,index)=>{
        return create_node(element.title,element.level,index,0);
    });
}

const Playground = () => {
    const {map} = useNodeMapContext();
    return (
        <div className='Playground'>
            {create_layout(map)}            
        </div>
    )
}

export default Playground;
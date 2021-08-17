import {useState} from 'react';
import { useNodeMapContext} from '../../Contexts/nodemap.js';
import './headers.css';
export const Header= ()=>{
    const {map,setMap} = useNodeMapContext();
    const [file,setFile]=useState('Select File');
    const save = (map,filename='map.json')=> {
         const blob = new Blob([JSON.stringify(map)],{type : 'application/json'});
         if (window.navigator.msSaveOrOpenBlob) // IE10+
            {window.navigator.msSaveOrOpenBlob(blob, filename); 
        }else {
            let a = document.createElement("a");
            let url = URL.createObjectURL(blob);
            console.log(url);
            a.download=filename;
            a.href=url;
            //let div=document.getElementById('file');
            //div.appendChild(a);
            a.click();
            /*setTimeout(()=>{div.removeChild(a);
                           window.URL.revokeObjectURL(url);
                        },0);
            */      
        }
    }
    const load = (content)=>{
        setMap(JSON.parse(content));
        window.location.reload();
    }
    const selectFile=(event)=>{
        var file = event.target.files[0];
        console.log(file);
        setFile(`File selected: ${file.name}`);
        let reader = new FileReader();
        reader.onload = (event)=>{
            load(event.target.result);
        }
        reader.readAsText(file);

    }
    return (
        <div className='headerClass'>
            <button className='btn' onClick={(e)=>{save(map)}}>Save File</button>
            <label htmlFor="filepicker" className='btn'>{file}</label>
            <input id='filepicker' type='file'  onChange={
                                (e)=>{selectFile(e);}
                                }
                    style ={{margin:'5px',visibility:'hidden'}} >
            </input>
        </div>
    );
}

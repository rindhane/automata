import React, { useState} from 'react';
import {Link} from 'react-router-dom';

import './Join.css';


/*const OtpField = ({check}) => {
    return (
        check ? (
        <div><input placeholder="OTP" className="joinInput" type="text" onChange={(event) => console.log(event.target.value)} /></div> )
        : 
        (<div></div>)
    )
}*/

const Join = ()=> {
    const [name,setName]=useState('');
    const [room,setRoom]=useState('');
    const [check,setCheck]=useState(true);

    return (
        <div className="joinOuterContainer">
            <div className="joinInnerContainer">
                <h1 className="heading">Join</h1>
                {//<OtpField check={check}/>
                }
                <div>
                        {//<input placeholder="91 (Country Code)" className="joinInput" type="text" onChange={(event) => console.log(event.target.value)} />
                        }
                        <input placeholder="Name" className="joinInput" type="text" onChange={(event) => setName(event.target.value)} />
                </div>
                <div><input placeholder="Room" className="joinInput mt-20" type="text" onChange={(event) => setRoom(event.target.value)} /></div>
                <Link onClick={event => (!name || !room) ? event.preventDefault(): null} to={`/chat/?name=${name}&room=${room}`}>
                    <button className="button" type="submit">Sign In</button>
                </Link>
            </div>
        </div>
    )
};

export default Join;
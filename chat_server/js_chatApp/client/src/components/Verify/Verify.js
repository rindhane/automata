import React, {useState,useEffect} from 'react';
import { Redirect } from "react-router-dom";
import { useSocket } from '../../context/socketProvider';


const Verify = ({location,mId,setId}) => {
    const [socket,setSocket]=useState();
    const [check,setCheck]=useState(false);
    const name=location.state.name;
    const mobile=location.state.mobile;
    const otp=location.state.otp;
    const verificationId=location.state.confirmation;
    let {SocketWorker} = useSocket();
    console.log('running multiple times');
    const ValidateOtp = (socket,name, mobile, otp, setCheck,verificationId) =>{
        setCheck(true);        
        socket.emit('otp',{name:name ,mobile: mobile, 
                    verificationId:verificationId ,otp:otp},(res,error) => {
            if (res) {
                console.log('where i am?');
                return true;
            }else {
                alert(error);
                socket.close();
                return false;
            }
        });
        return true;
    };
    const socketListener=(socket)=>{
        socket.on('getToken',({id,mobile,token,name,gcredential})=>{
            setId({id,mobile,token,name,gcredential});
            socket.close();
        })
    }

    useEffect( ()=>{
        let socket = SocketWorker();
        setSocket(socket);
        ValidateOtp(socket, name, mobile, otp, setCheck,verificationId);
    },[]);

    useEffect(()=>{
        if (check) {
            socketListener(socket); 
        }
    },[check])

   

    return ( mId ? <Redirect to={'/chat'} />
            : (<div> 
                <p>The otp is under verification</p> 
            </div>) );

}

export default Verify;
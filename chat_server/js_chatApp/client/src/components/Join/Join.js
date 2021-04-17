import React, { useState, useRef, useEffect} from 'react';
import {Link} from 'react-router-dom';
import { useSocket } from '../../context/socketProvider';
import './Join.css';
import {firebase,useFirebase} from "../../context/firebaseProvider";
import PhoneInput from 'react-phone-number-input';
import 'react-phone-number-input/style.css'



const reverse = (val) => {
    return !val;    
}

const OtpField = ({check,setVal}) => {
    return (
        check ? (
        <div><input placeholder="OTP" className="joinInput" type="text" onChange={(event) => setVal(event.target.value)} /></div> )
        : 
        (<div></div>)
    )
}

const validateMobile = async (val,auth,captcha,setConfirmation, getAuth) =>{
    let ans = false;
    if (val){
        const number=val.toString().replace('+',"");
        if(number.length<11 || number.length>12){
            return false;
        }else if(number.match(/\D/)){
            return false;
        }else {
            await auth.signInWithPhoneNumber(val,captcha).
            then(function(confirmationResult){
                ans=true;
                setConfirmation(confirmationResult.verificationId);
                //console.log('confirmation',confirmationResult);
                getAuth(val,confirmationResult.verificationId);
                console.log('auth sent');
            }).catch((error)=>{
                console.log(error);
            })
            return true;
        }
    }
    return false;
}


const captchaVerifier = (ref,setAllow) =>{
    const captcha=new firebase.auth.RecaptchaVerifier(ref,{
        'size': "small",
        'callback': (response) =>{
            console.log("allowSingin");
            setAllow(true);

        },
        'expired-callback':()=>{
            console.log('refresh captcha');
        }
    });
    captcha.render().then(function(widgetId){
        console.log(widgetId);
    })
    return captcha
}

const submitOtp = (event, name, mobile, otp, submitMobile,confirmation,socket)=>{

    if (!name || !mobile || !otp || submitMobile!=mobile ) 
    {
        event.preventDefault()
        if (submitMobile!=mobile) {
            alert("Mobile Changed, refresh and submit the correct mobile again")
        };
    } else {
    (()=>{console.log('confirmation submitted');socket.close()})() }; 
}

const Join = ({ mId, onSetId})=> {
    const [name,setName]=useState('');
    const [mobile,setMobile]=useState("");
    const [submitMobile,setSubmitMobile]=useState("");
    const [otp,setOtp]=useState("");
    const [room,setRoom]=useState('chatRoom');
    const [check,setCheck]=useState(false);
    const {SocketWorker} = useSocket();
    const [allowOtp,setAllow]=useState(false);
    const captchadiv=useRef();
    const [captcha,setCaptcha]=useState();
    const [confirmation,setConfirmation]=useState('');
    const {auth}=useFirebase();
    const [Msocket,setMSocket]=useState();

    const getAuth = (mobile,verificationId) => {
        setSubmitMobile(mobile);
        const socket= SocketWorker();
        setMSocket(socket);
        socket.emit('initiateUser', {mobile: mobile,verificationId:verificationId},(res,error) => {
            if (res) {
                socket.emit("disarm");
                socket.close();
                return true;
            }else {
                alert(error);
                socket.emit("disarm");
                socket.close();
                return false;
            }
        });
        setCheck(reverse(check));
    }

    const setField =(val)=> {
        setRoom(val);
        setMobile(val);
    }
    useEffect(()=>{
        setCaptcha(captchaVerifier("captcha-container",setAllow));
    },[])

    return (
        <div className="joinOuterContainer">
            <div className="joinInnerContainer">
                <h1 className="heading">Join</h1>
                <div>
                    {/*    <input placeholder="91 (Country Code)" className="joinInput" type="text" onChange={(event) => setCode(event.target.value)} />
                        <input placeholder="Mobile" className="joinInput" type="text" onChange={(event) => setField(event.target.value)} />
                    */}
        
                    <div className='PhoneInput'>
                        <PhoneInput 
                        placeholder="Enter phone number"
                        countryCallingCodeEditable={false}
                        defaultCountry="IN"
                        international 
                        value={mobile} 
                        onChange={setField}/>
                    </div>
                    <br/>
                    <OtpField check={check} setVal={setOtp}/>
                    <button disabled={!allowOtp} className="button" type="submit" style={{display : (check ? 'none' : 'block') }} onClick={(event)=>(!validateMobile(mobile,auth,captcha,setConfirmation, getAuth) || !mobile) ? event.preventDefault() : null}> Get OTP </button>
                </div>
                <input placeholder="Name" style={{display : (check ? 'block' : 'none') }} className="joinInput mt-20" type="text" onChange={(event) => setName(event.target.value)} />
                <Link onClick={event=>{submitOtp(event, name, mobile, otp, submitMobile,confirmation,Msocket)}} 
                      to={{ pathname:`/verify`,
                            state: {
                                name:name,
                                room:room,
                                mobile:mobile,
                                otp:otp,
                                confirmation:confirmation,
                            }
                            }}>
                    <button style={{display : (check ? 'block' : 'none') }} className="button" type="submit">Sign In</button>
                </Link>
                <br/>
                    <div ref={captchadiv} id="captcha-container"></div> 
            </div>
        </div>
    )
};

export default Join;
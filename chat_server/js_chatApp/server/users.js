const {v4} = require('uuid');
const {firebase, app,admin} = require ('./init-firebase');

const users = [];


const generateKey = ({code,mobile}) => {
    return v4();
}

const generateId = ()=>{
    return v4();
}

const SCHEMA = {
    users : 'users',
    messages: 'messages',
}

const loadUsers = async ()=> {
    const db = admin.firestore();
    const snapshot = await db.collection(SCHEMA.users).get();
    snapshot.forEach(user=>users.push({
        ...user.data()
    }));
} 

(async()=>{
await loadUsers();
})()

const UpdateUserBackend = (user) =>{
    const db = admin.firestore();
    const docRef = db.collection(SCHEMA.users).doc(user.mobile);
    (async ()=>{
        await docRef.set({...user})
    })();
} 


const liveUsers= [];

const addLiveUser = (user) =>{
    return liveUsers.push(user);
}

const getLiveUser= (id)=>{
    return liveUsers.find(user=>user.id===id);
}

const removeUser = (id) => {
    const index=liveUsers.findIndex((user)=>user.id ===id);
    if(index!==-1) {
        return liveUsers.splice(index,1)[0];
    }
}

const getNewUser=({mobile}) => {
    if (MasterUser().mobile===mobile){return MasterUser()};
    return users.find((user)=>user.val===mobile);
}

const getUser=(id) => {
    return users.find((user)=>user.id===id)
}

const getUsersInRoom = () => {
    return liveUsers.map((user)=> {return user.id});
}

const initiateUser = ({id,mobile,token,verificationId}) => {
    let user;
    if (getNewUser({mobile})) {
        user = getNewUser({mobile});
        user.token=token;
        user.verificationId=verificationId;
        //console.log('oldinitiation',user,users);
        UpdateUserBackend(user);
    } else {
        user = {id,mobile:mobile,val:mobile,token,verificationId};
        users.push(user);
        UpdateUserBackend(user);
        //console.log('newinitiation',user,users);   
    }
    return {user:user};
}

const isOtpValid = async (user,otp, verificationId)=> {
    let credential={};
    if (user.verificationId==verificationId){
    credential = firebase.auth.
                        PhoneAuthProvider.
                        credential(verificationId,otp);
    }                    
    let ans = undefined;
    await app.auth()
                .signInWithCredential(credential)
                .then(resultUser=>{ans=credential.toJSON();
                    app.auth().signOut()
                            .then(()=>console.log('authsuccessful'))
                            .catch(error=>console.log(`error in loggingIn:${error}`))
                })
                .catch(error=>console.log(error))
    return ans;
}

const MasterUser = ()=>  {
    return users.find((user)=>{return user.val=='ultimateAdmin'});
}


const sendMessage=({
    sender:senderId,
    recipient:recipientId,
    senderName:senderName,
    text:Messagetext
    })=>{
    const message= {
        senderID:senderId,
        recipientID:recipientId,
        text:Messagetext,
        name:senderName,
        time:admin.firestore.FieldValue.serverTimestamp()
    }
    const db = admin.firestore();
    const sender = db.collection(SCHEMA.users)
                    .doc(getUser(senderId).mobile)
                    .collection(SCHEMA.messages)
                    .doc();
    const receiver = db.collection(SCHEMA.users)
                    .doc(getUser(recipientId).mobile)
                    .collection(SCHEMA.messages)
                    .doc();
    (async ()=>{
        await receiver.set(message);
                    })();
    (async ()=>{
        await sender.set(message);
    })();
}

module.exports= {removeUser, 
                getUser,
                getUsersInRoom , 
                isOtpValid, 
                generateKey,
                initiateUser, 
                getNewUser, 
                generateId, 
                MasterUser, 
                addLiveUser, 
                getLiveUser,
                UpdateUserBackend,
            sendMessage };


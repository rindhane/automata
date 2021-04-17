import React, {useContext, useState ,useEffect} from 'react';
import firebase from 'firebase/app';
import 'firebase/auth';

const firebaseContext = React.createContext();
export {firebase};
export function useFirebase() {
    return useContext(firebaseContext);
}


export function FirebaseProvider ({children}){

    const [auth, setAuth ]=useState();
    const [setupDone,setSetup]=useState(false);
    const [currentUser,setCurrentUser]=useState();

    useEffect(()=>{
        const app = firebase.initializeApp(
            {
                apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
                authDomain: process.env.REACT_APP_FIREBASE_AUTHDOMAIN,
                projectId: process.env.REACT_APP_FIREBASE_PROJECTID,
                storageBucket: process.env.REACT_APP_FIREBASE_STORAGEBUCKET,
                messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGINGSENDERID,
                appId: process.env.RREACT_APP_FIREBASE_APPID,
                measurementId: process.env.REACT_APP_FIREBASE_MESASUREMENTID
            },
        );
        const tmpAuth=app.auth()
        setAuth(tmpAuth);
        const unsubscribe = tmpAuth.onAuthStateChanged(user=>{
            setCurrentUser(user);
            setSetup(true);
    
        })
        return unsubscribe;
    },[]);

    //const checkPhone        
    //auth.useDeviceLanguage();

    const value={
        auth,
        currentUser,
        firebase
    };

    return (
        <firebaseContext.Provider value = {value}>
            {setupDone && children}
        </firebaseContext.Provider>
    )
}
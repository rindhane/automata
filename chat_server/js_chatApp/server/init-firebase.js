var firebase = require('firebase/app');
const {admin}= require('./adminFirebase');
require("firebase/auth");

const firebaseClientConfig="./creds/config.json"
var firebaseConfig = require(firebaseClientConfig);
// Initialize Firebase
var app= firebase.initializeApp(firebaseConfig);


module.exports={
    firebase,
    app,
    admin
}


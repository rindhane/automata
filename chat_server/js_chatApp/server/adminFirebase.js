
var admin = require("firebase-admin");



//SERVER_CRED = "path/to/credentials.json"
//var serviceAccount = require(SERVER_CRED);
//OR
//using GOOGLE_APPLICATION_CREDENTIALS from environment instead of SERVER_CRED
admin.initializeApp({
  //credential: admin.credential.cert(serviceAccount)
  credential: admin.credential.applicationDefault(),
});


module.exports={
  admin,
}
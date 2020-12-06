'use strict';
const fs = require('fs');
const {oauth}=require('./oauth');
const {google} = require('googleapis');
const { file } = require('googleapis/build/src/apis/file');

//constant values
const TOKEN_PATH = 'token.json';
const CREDENTIALS = 'credentials.json';


function uploadFile(auth) {
    const drive = google.drive({version: 'v3', auth});
    var fileMetadata = {
        'name': 'MFL67584519.pdf',

    };
    var media = {
        mimeType: 'application/pdf',
        body: fs.createReadStream('MFL67584519.pdf')
      };
    drive.files.create({
        resource: fileMetadata,
        media:media,
        field:'id',
        uploadType:'multipart'
    } ,
        function(err,res){
            if (err){
                console.log(err);
                    }else {
                        console.log ("File details ", res.data);
                    }; 
        });
  };

let filedetails= '';
let i =1;

function fileDetails(auth) {
    const drive = google.drive({version: 'v3', auth});
    drive.files.get(
        {
        fileId : filedetails,
        fields: '*',
        },
    function(err,res)
    {
        if (err){
            console.log(err);
                }else {
                    console.log ("File details ", res);
                    if (res.data){
                        if (res.data.parents && i<4) {
                            filedetails=res.data.parents;
                            oauth({
                                TOKEN_PATH: TOKEN_PATH,
                                credentials:CREDENTIALS,
                                callback:fileDetails
                              });
                              i++;
                                                  };
                                };
                    };
    } 
                    );   
};

oauth({
  TOKEN_PATH: TOKEN_PATH,
  credentials:CREDENTIALS,
  callback:fileDetails
}); 

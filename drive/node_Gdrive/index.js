'use strict';
const fs = require('fs');
const {oauth}=require('./oauth');
const {google} = require('googleapis');

//constant values
const TOKEN_PATH = 'token.json';
const CREDENTIALS = 'credentials.json';


function listFiles(auth) {
    const drive = google.drive({version: 'v3', auth});
    drive.files.list({
      pageSize: 10,
      fields: 'nextPageToken, files(id, name, parents, webContentLink,webViewLink, kind, spaces,mimeType)',
    }, (err, res) => {
      if (err) return console.log('The API returned an error: ' + err);
      const files = res.data.files;
      if (files.length) {
        console.log('Files:');
        files.map((file) => {
          console.log(`${file.name} (${file.id}) <${file.parents}>`);
        });
      } else {
        console.log('No files found.');
      }
    });
  };

oauth({
  TOKEN_PATH: TOKEN_PATH,
  credentials:CREDENTIALS,
  callback:listFiles
}); 
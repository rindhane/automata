#! /usr/bin/env bash

cd client
npm start &
echo 'switching to server'
export PORT=8080 ;  
cd ../server
export GOOGLE_APPLICATION_CREDENTIALS='./creds/admin-firebase.json'
npm start &

#! /usr/bin/env bash

cd ./client
rm -r build
npm run build
cd ../ 
rm -r ./deployment/*
rsync -av --progress ./server/ ./deployment --exclude node_modules
rm -r ./deployment/build
rsync -av --progress ./client/build ./deployment/
cp app.yaml ./deployment/ 
cd deployment 
gcloud app deploy #make sure right project is selected in gcloud config set

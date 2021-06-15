#! /usr/bin/env bash

#key-variables
#replace <place holder> with exact value
serviceAccount='<account Name>'
project_ID='<project id >'
fileName='<file name.json>'

#first create service account 
gcloud iam service-accounts create $serviceAccount

#grant permissions to service account 
gcloud projects add-iam-policy-binding $project_ID --member="serviceAccount:${serviceAccount}@${project_ID}.iam.gserviceaccount.com" --role="roles/owner"

#create key file for client
gcloud iam service-accounts keys create $fileName --iam-account=${serviceAccount}@${project_ID}.iam.gserviceaccount.com

#! /usr/bin/env python

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os 
import json
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def client_properties(filePath='credentials.json'):
    client_detatils_path=filePath
    scopes = ['https://www.googleapis.com/auth/drive.metadata.readonly',
                'https://www.googleapis.com/auth/drive.file']
    redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
    return client_detatils_path, scopes, redirect_uri


def get_user_authenticated(client, scopes, url):    
    flow = Flow.from_client_secrets_file(
    client,
    scopes= scopes, 
    redirect_uri=url)
    auth_uri, _ = flow.authorization_url(prompt='consent')
    print('Go to url to get the code : \n')
    print(auth_uri,'\n')
    code =input ('enter the code here  and press enter: ')
    try :
        flow.fetch_token(code=code)   
        return flow.credentials
    except : 
        return None
def storeUserCred(userFile,creds):
    with open(userFile, 'w') as token:
        token.write(creds.to_json())

def isUserAvailable(userFile):
    credentials=None
    if os.path.exists(userFile):
        try :
            credentials = Credentials.from_authorized_user_file(
                                userFile, 
                                json.load(open(userFile,'r')).get('scopes'),
                                )
            if not credentials.valid :
                credentials=None
            elif credentials.expired and credentials.refresh_token:
               credentials.refresh(Request())
        except: 
                credentials=None #check is pass statement can be used here 
    return credentials

def get_drive_auth(filePath='token.pickle',clientPath='credentials.json'):
    API_SERVICE_NAME = 'drive' 
    API_VERSION ='v3'
    credentials = isUserAvailable(userFile=filePath)
    if credentials:
        return build(API_SERVICE_NAME, API_VERSION,credentials=credentials)
    else:
        credentials=get_user_authenticated(*client_properties(clientPath))
        if credentials :  
            storeUserCred(filePath,credentials)
            return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    return None    
if __name__ == '__main__':
    pass      




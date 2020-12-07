#! /usr/bin/env python

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os 
import pickle

def client_properties(filePath='credentials.json'):
    client_detatils_path=filePath
    scopes = ['https://www.googleapis.com/auth/drive.metadata.readonly',
                'https://www.googleapis.com/auth/drive.file']
    redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
    return client_detatils_path, scopes, redirect_uri


def get_credentials(client, scopes, url):    
    flow = Flow.from_client_secrets_file(
    client,
    scopes= scopes, 
    redirect_uri=url)
    auth_uri, _ = flow.authorization_url(prompt='consent')
    print('Go to url to get the code : \n')
    print(auth_uri,'\n')
    code =input ('enter the code here  and press enter: ')
    flow.fetch_token(code=code)    
    return flow.credentials

def get_drive_auth(filePath='token.pickle'):
    API_SERVICE_NAME = 'drive' 
    API_VERSION ='v3'
    if os.path.exists(filePath):
        with open(filePath, 'rb') as token:
            credentials = pickle.load(token)
        return build(API_SERVICE_NAME, API_VERSION,credentials=credentials)
    else:
        client,scopes,url=client_properties('credentials.json')
        credentials=get_credentials(client,scopes,url)
        if credentials:
            with open(filePath, 'wb') as token:
                token.write(pickle.dumps(credentials))
        return build(API_SERVICE_NAME, API_VERSION,credentials=credentials)
        
if __name__ == '__main__':
    pass      



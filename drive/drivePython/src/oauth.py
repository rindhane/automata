#! /usr/bin/env python

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os 
import json
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class Config_Manager():
    #move this manager to helper_file
    #master class to handle the configuration for an application
    def __init__(self,file_path="config.json") -> None:
        print(f"Following config path has been set: {self.set_config_file(file_path)}")
    def set_config_file(self,file_path:str):
        self.file_path=file_path
        return self.file_path
    def read_config_as_dict(self):
        with open(self.file_path,'r') as file :
            temp=json.loads(file.read())
        return temp

class Credentials_property_manager(Config_Manager):
    #this class creates the 
    def __init__(self, file_path):
        super().__init__(file_path=file_path)
        self._load(self.read_config_as_dict())
    def client_properties(self):
        return self.client_secret, self.scopes,self.redirect_uri
    def storeUserCred(self,creds):
        with open(self.token, 'w') as token:
            token.write(creds.to_json())
    def _load(self,data_dict):
        dict_keys=['scopes', 'redirect_uri', 'API_SERVICE_NAME', 'API_VERSION', 'client_secret', 'token']
        for key in dict_keys:
            setattr(self,key,data_dict[key])
        return True


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

def isUserAvailable(userFile):
    credentials=None
    if os.path.exists(userFile):
        try :
            credentials = Credentials.from_authorized_user_file(
                                userFile, 
                                json.load(open(userFile,'r')).get('scopes'),
                                )
            if not credentials.valid :
                if credentials.expired and credentials.refresh_token:
                    credentials.refresh(Request())
        except: 
                pass #check is pass statement can be used here 
    return credentials

def get_drive_auth(cred_provider:Credentials_property_manager): 
    """
    Details: 
    This function returns the object authenticated with the google drive manger to access the files 
    """
    credentials = isUserAvailable(userFile=cred_provider.token) #check whether is their client creds are stored in the cred_provider
    if credentials:
        return build(cred_provider.API_SERVICE_NAME, cred_provider.API_VERSION,credentials=credentials)
    else:
        credentials=get_user_authenticated(*cred_provider.client_properties())
        if credentials :  
            cred_provider.storeUserCred(credentials)
            return build(cred_provider.API_SERVICE_NAME, cred_provider.API_VERSION, credentials=credentials)
    return None    

if __name__ == '__main__':
    pass      




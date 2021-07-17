#! /usr/bin/env python
from evernote.api.client import EvernoteClient
from src_python.utilities import ( get_secret_details, 
                                   save_secret_details, 
                                )


def run_verification(client_dict,callback_url):
    client=EvernoteClient(**client_dict)
    token=client.get_request_token(callback_url=callback_url)
    return client,token

def get_user_authorization(client, token):
    url=client.get_authorize_url(token)
    print('go to url & authorize:\n',url)
    verifier=input('enter the verifier:')
    return verifier

def get_client(auth_path=None,client_path=None):
    try:
        auth=get_secret_details(auth_path)
        return EvernoteClient(token=auth["oauth_token"])
    except:
        CLIENT_SECRET=get_secret_details(client_path)
        client,token=run_verification(
                        client_dict=CLIENT_SECRET,
                        callback_url=CLIENT_SECRET['callback_url'])
        oauth_verifier=get_user_authorization(client,token)    
        result_dict=client.get_access_token_dict(
                                token['oauth_token'],
                                token['oauth_token_secret'],
                                oauth_verifier
                                )
        save_secret_details(result_dict,auth_path)
        return client

if __name__=='__main__':
    client=get_client(
        auth_path='../secrets/auth.json',
        client_path='../secrets/client.json'
            )
    print(client.get_user_store().getUser().name)
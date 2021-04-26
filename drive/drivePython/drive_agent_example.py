#! /usr/bin/env python

#Reference : https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html

from __future__ import print_function
from googleapiclient.discovery import build 
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
USER_SECRET='drive_token.json'
CLIENT_SECRET='client_secret.json'
def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    if os.path.exists(USER_SECRET):
        try :
            creds = Credentials.from_authorized_user_file(USER_SECRET, SCOPES)
        except: 
            creds= None 
    else: 
        creds = None
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET, scopes=SCOPES)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open(USER_SECRET, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        #pageSize=10, fields="nextPageToken, files(id, name)"
        ).execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id'],item['mimeType']))


if __name__ == '__main__':
    main()
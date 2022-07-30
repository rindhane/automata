#! /usr/bin/env python

from src.oauth import get_drive_auth , Credentials_property_manager

#prepare the credentials manager
credentials_record=Credentials_property_manager(file_path="config.json")

#test run the google drive manager
print(get_drive_auth(credentials_record).files().list().execute())
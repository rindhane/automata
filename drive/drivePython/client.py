#! /usr/bin/env python
from oauth import get_drive_auth
import json

def get_drive():
    tmp = get_drive_auth(filePath='token.pickle',clientPath='credentials.json')
    if tmp :
        return tmp
    else :
        raise Exception("User not Authenticated")  


def walk_drive(callback):
    drive=get_drive()
    schema='files(id, name, size, mimeType ,appProperties,version,\
                    originalFilename, description,owners, quotaBytesUsed, \
                    md5Checksum, webContentLink, spaces, headRevisionId,\
                    shortcutDetails,sharingUser,ownedByMe)'
    http_req = drive.files().list(
        pageSize=1000, fields=f"nextPageToken, {schema}",)

    while http_req is not None : 
        files=http_req.execute()
        callback(drive,files.get('files',[]))
        http_req=drive.files().list_next(http_req,files)

def get_root(drive,id_):
    schema='id, parents'
    result=drive.files().get(fileId=id_, 
                            fields=f'{schema}').execute()
    parent=result.get('parents', None)
    if type(parent)==type(list()):
        return get_root(drive,parent[0])
    elif parent is None :
        return id_
    else:
        raise ValueError (f"something wrong in parents of {id_}")

def create_path(drive, id_, path = []):
    result=drive.files().get(fileId=id_, 
                            fields='id, name, parents').execute()
    parent=result.get('parents', None)
    if type(parent)==type(list()):
        path=list(path)
        path.insert(0,id_)
        return create_path(drive, parent[0],path)
    elif parent is None :
        path=list(path)
        path.insert(0,id_)
        return path
    else:
        raise ValueError (f"something wrong in parents of {id_}")

def print_id(files_list):
    for file_schema in files_list:
        print(file_schema.get('name'),
            ' ', file_schema.get('parents',None) )


def make_jsonIndex(drive,files_list,index=dict()):
    for file_schema in files_list:
        file_id=file_schema.get('id')
        path=create_path(drive,id_=file_id)
        index[file_id] = file_schema
        index[file_id].update({'path': path})
        print(index[file_id])
    fp=open('index.json','w')
    fp.write(json.dumps(index))
    fp.close()
    print("Path of all files have been printed")


if __name__== "__main__":
    walk_drive(make_jsonIndex)

    
#! /usr/bin/env python
from oauth import get_drive_auth


def get_drive():
    return get_drive_auth(filePath='token.pickle',clientPath='credentials.json')


def walk_drive(callback):
    drive=get_drive()
    schema='files(id, name, parents)'
    http_req = drive.files().list(
        pageSize=1000, fields=f"nextPageToken, {schema}",)

    while http_req is not None : 
        files=http_req.execute()
        callback(drive,files.get('files',[]))
        http_req=drive.files().list_next(http_req,files)

def get_root(drive,id_):
    result=drive.files().get(fileId=id_, 
                            fields='id, name, parents').execute()
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


def get_filePath(drive,files_list):
    for file_schema in files_list:
        path=create_path(drive,id_=file_schema.get('id'))
        print(file_schema.get('name'), ' ', path)
    print("Path of all files have been printed")

if __name__== "__main__":
    walk_drive(get_filePath)

    
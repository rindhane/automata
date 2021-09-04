from getTOTP import getFernet, file
import json

def getDict():
    message = open(file,'rb').read()
    f=getFernet() 
    token=f.decrypt(message)
    token=json.loads(token)
    return token

def storeDict(newDict):
    fp= open(file,'wb')
    f=getFernet()
    dump=json.dumps(newDict)
    encryptedData=f.encrypt(dump.encode())
    fp.write(encryptedData)
    fp.close()
    print(f'{file} has written with newData')
    return fp


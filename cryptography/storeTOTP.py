from getTOTP import getFernet, file
import json
import re 

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

#url format: otpauth://totp/TOTP_INSTANCE_NAME?secret=SECRET_ALPHA_NUMERIC_CHARACTERS&amp;issuer=ISSUER_NAME
def create_dict_item_from_url(url,providerName):
    chrs=['user','secret','issuer']#characteristics(chrs) details to obtain 
    expression=f'otpauth://totp/(?P<{chrs[0]}>.*)?secret=(?P<{chrs[1]}>.*)&amp;issuer=(?P<{chrs[2]}>.*)$'
    search=re.search(expression,url)
    result=dict()
    for tag in chrs : 
        result[tag]=search.group(tag)
    return {providerName:result}

def get_new_dict_to_store(old_dict,item_dict):
    return dict(**old_dict,**item_dict)

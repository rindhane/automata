from getTOTP import getFernet, file
import json
import re 
import sys
import json
import os 

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
def create_dict_item_from_url(url,providerName,printResult=False):
    chrs=['user','secret','issuer']#characteristics(chrs) details to obtain 
    expression1=f'otpauth://totp/(?P<{chrs[0]}>.*)?secret=(?P<{chrs[1]}>.*)&amp;issuer=(?P<{chrs[2]}>.*)$' #old
    expression=f'^otpauth://totp/(?P<{chrs[0]}>.*)\?secret=(?P<{chrs[1]}>.*)&issuer=(?P<{chrs[2]}>.*)$' #new
    search=re.search(expression,url)
    result=dict()
    if search : 
        for tag in chrs :
            try :  
                result[tag]=search.group(tag)
                if printResult :
                    print(tag,":",result[tag])
            except : 
                print(f"following tag was not captured {tag}")
        return {providerName:result}
    return None

def get_new_dict_to_store(old_dict,item_dict):
    return dict(**old_dict,**item_dict)

def write_env_file(content,fileName=".env"):
    env_file = open(fileName,"w")
    env_file.write(content)
    env_file.close()

def read_from_env_file(fileName=".env"):
    env_file=open(fileName,'r')
    content=env_file.read()
    env_file.close()
    return content

def read_newItem_url(fileName=".env"):
    content = read_from_env_file(fileName)
    splits= content.split(':-')
    return splits[1].strip()


def clean_env_variables (fileName=".env"):
    os.remove(fileName)


if __name__=="__main__":
    if len(sys.argv)<2:
        print("please provide the command")
        sys.exit(1)
    if sys.argv[1]=="printOld":
        result = getDict()
        content = json.dumps(result)
        print(content)
        sys.exit(0)
    if sys.argv[1]=="postNewItem":
        if len (sys.argv)<3 :
            print("provide 3 arg as provider name" ) 
            sys.exit(1)
        content  = read_newItem_url()
        r=create_dict_item_from_url(content,sys.argv[2],printResult=False)
        write_env_file(json.dumps(r))
        sys.exit(0)
    if sys.argv[1]=="insert":
        old = getDict()
        new = json.loads(read_from_env_file())
        result = get_new_dict_to_store(old,new)
        write_env_file(json.dumps(result))
        sys.exit(0)
    if sys.argv[1]=="store":
        new = json.loads(read_from_env_file())
        storeDict(new)
        sys.exit(0)
    if sys.argv[1]=="clean":
        clean_env_variables()
    print('error, it reached the end but nothing got executed')
    sys.exit(2)
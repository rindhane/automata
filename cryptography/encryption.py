#! /usr/bin/env python

#encrypting and decrpyting text with password
#help: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys


def main(fileName=None) : 
    password=input("provide the password :").encode()
    #salt=os.urandom(16)
    salt2=b'\x17JA]C{\x0f2\xecIi\x0c>\xaei\x16'
    kdf=PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt2,
        iterations=10**7,
    )
    key=base64.urlsafe_b64encode(kdf.derive(password))
    f=Fernet(key)
    tmp=input('enter 1 for encryption or enter 2  for decryption :')
    if tmp=='1':
        #help for multiline: https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user
        if fileName == None :
            print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it. \n")
            contents = [] 
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                contents.append(line)
            message = '\n'.join(contents)
            print('\n')
            print('encrypted bytes>> \n')
            print(token)
        else :
            message = get_file_content(fileName)
            token=f.encrypt(message.encode()) 
            write_file_content(fileName,token.decode()) 
    if tmp =='2':
        if fileName==None : 
            message=input('enter all bytes displayed as string \n')
        else : 
            message = get_file_content(fileName)
        token=f.decrypt(message.encode())
        if fileName==None : 
            print('\n resultant text \n')
            print(token.decode())
        else : 
            write_file_content(".temp",token.decode())
    print('\n\n process is complete \n\n')

def get_file_content(fileName) :
    fp=open(fileName,"r")
    content = fp.read()
    fp.close()
    return content

def write_file_content(fileName,content):
    fp=open(fileName,"w")
    fp.write(content)
    fp.close()



if __name__=="__main__" :
    if len(sys.argv)<2 :
        main()
        sys.exit(0)
    main(fileName=sys.argv[1])
    sys.exit(0)
#! /usr/bin/env python

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import pyotp
import json

file='./TOTPsecret.file'

def getFernet():
    #prepare salt from the input
    salt_prior=b'\xc9\x07\xfcF\x85\x82Kq\xbe\x99\xa2\xa8\x8b\x0e\x84E<\x16\xaa\x8f"\x9f\xff\xc4)\xf7~\x0c\x0e\x94D\x11'
    salt_back=b'F\xcev\xd9)\xecS\xce\xe8\xd5\xe0\x1fJr\xdd|\x19\x9ca\xdesj\xcb\x00\x04\x08\x98`*\x9a\x83L'
    salt_input=input("provide the salt passphrase:").encode()
    saltHash=hashlib.sha256(salt_input).digest()
    salt=salt_prior+saltHash+salt_back
    kdf=PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10**7,
    )
    password=input("provide the password:").encode()
    key=base64.urlsafe_b64encode(kdf.derive(password))
    f=Fernet(key)
    return f

if __name__=='__main__':
    #implement token retrieval
    message = open(file,'rb').read()
    f=getFernet() 
    token=f.decrypt(message)
    #end token retrieval
    token=json.loads(token)
    token=token[input('enter the provider name:')]
    totp=pyotp.TOTP(token['secret'].encode())
    print(totp.now())

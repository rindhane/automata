#! /usr/bin/env python

#encrypting and decrpyting text with password
#help: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it. \n")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    message = '\n'.join(contents)
    token=f.encrypt(message.encode())
    print('\n')
    print('encrypted bytes>> \n')
    print(token)
if tmp =='2':
    message=input('enter all bytes displayed as string \n')
    token=f.decrypt(message.encode())
    print('\n resultant text \n')
    print(token.decode())

print('\n\n process is complete \n\n')
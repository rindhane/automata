#credits
#https://stackoverflow.com/questions/39074253/extract-publickey-from-privatekey-input-using-python


from Crypto.PublicKey import RSA
from base64 import b64decode

def getkey(fileName):
    checker='RSA PRIVATE KEY'
    key_in_text=''
    with open(fileName,'r') as fp:
        a=fp.readline()
        while a !='':
            if checker not in a:
                key_in_text=key_in_text+a.replace('\n','')
            a=fp.readline()
    return key_in_text

pem_key=getkey('trialNew.pem').encode()
key=b64decode(pem_key)
keyPriv = RSA.importKey(key)
print(keyPriv)
publickey=keyPriv.publickey().exportKey('PEM')
print(publickey)
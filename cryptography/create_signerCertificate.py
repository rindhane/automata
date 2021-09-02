#! /usr/bin/ env python

import cryptography as lib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography import x509
import base64
import datetime as dt
import os
from dataclasses import dataclass, field
import json

#pending  
#certificatehandler
    #save to file path
    #for both authenticator & new user
        # shifting Name attribute to functional setup
    # add argument create functional for certifier in new function  

def NameAttributeFunctions(val):
    NameOID=x509.oid.NameOID
    if val=='countryName':
        return NameOID.COUNTRY_NAME
    if val=='stateName':
        return NameOID.STATE_OR_PROVINCE_NAME
    if val=='organization':
        return NameOID.ORGANIZATION_NAME
    if val=='commonName':
        return NameOID.COMMON_NAME
    if val=='pseudnoym':
        return NameOID.PSEUDONYM
    if val=='telNumber':
        return x509.ObjectIdentifier(dotted_string='2.5.4.20')
    if val=='title':
        return NameOID.TITLE
    if val=='postalCode':
        return x509.ObjectIdentifier(dotted_string='2.5.4.17')
    if val=='organizationUnit':
        return NameOID.ORGANIZATIONAL_UNIT_NAME
    if val == 'subj_serial_number':
        return NameOID.SERIAL_NUMBER
    if val=='street' :
        return NameOID.STREET_ADDRESS
    if val=='houseIdentifier':
        return x509.ObjectIdentifier(dotted_string='2.5.4.51')
    raise Exception (f'{val} is not a valid attribute for conversion ')

def kwargs_to_NameAttribute(kwargs):
    result=[]
    keys=['countryName','stateName', 'organization', 
         'commonName','pseudnoym','telNumber','title',
         'postalCode','organizationUnit','subj_serial_number',
         'street','houseIdentifier',
        ]
    for key in keys:
        if kwargs.get(key):
            result.append(
                x509.NameAttribute(
                    NameAttributeFunctions(key),
                    kwargs.get(key)
                                  )
            )
    return result

@dataclass
class CertificateProps:
    """Class for creating new detail object about a certificate """
    #---minimum required----
    commonName:str
    countryName:str
    stateName: str
    organization: str
    email : str
    postalCode : str
    filePath: str
    #---optionally required----
    telNumber: str = field(default=None)
    title: str = field(default=None)
    organizationUnit:str = field(default=None)
    houseIdentifier:str = field(default=None)
    street:str = field(default=None)
    def toJson(self):
        pathVar='filePath'
        filePath=getattr(self,pathVar)
        delattr(self,pathVar)
        tmpDict=vars(self)
        open(filepath,'w').write(json.dumps(tmpDict))
    @classmethod
    def fromJson(cls,filePath):
        data=json.loads(open(filePath,'r').read())
        data['filePath']=filePath
        return cls(**data)
    def return_vals(self):
        return vars(self)

class CertSignRequestBuilder:
    def get_key_pair(self):
        return getattr(self,'_keyObject',None)
    def create_key_pair (self,public_exponent=65537,
                    key_size=2048,):
        creator=rsa.generate_private_key
        self._keyObject=creator(public_exponent=public_exponent,
                                key_size=key_size)
        return self._keyObject
    def create_certificate(self,**kwargs):
        builder=x509.CertificateSigningRequestBuilder()
        builder=builder.subject_name(
            x509.Name( kwargs_to_NameAttribute(kwargs))
        )
        builder=builder.add_extension(
            x509.SubjectAlternativeName([
            x509.RFC822Name(kwargs.get('email')),
                                        ]),
            critical=False,
                            )
        hashes=lib.hazmat.primitives.hashes
        self.csr=builder.sign(private_key=kwargs.get('key'),
                                algorithm=hashes.SHA256()
                              )
        return self.csr 

class Certify :
    def signer_inputs(self,csr,issuer_cert,**kwargs) :
        #input for kwaargs:
        #duration#int for days,
        #csr must be signing request
        #issuer_cert must be Certificate object
        cert=x509.CertificateBuilder()
        cert=cert.subject_name(csr.subject)
        cert=cert.issuer_name(
            issuer_cert.subject
        )
        cert=cert.public_key(csr.public_key())
        cert=cert.serial_number(
            int(''.join(map(lambda x: str(ord(x)),
                        base64.b64encode(os.urandom(2)).decode()
                        )
                    ))
        )
        cert=cert.not_valid_before(
            dt.datetime.utcnow()
        )
        cert=cert.not_valid_after(
            dt.datetime.utcnow() + dt.timedelta(days=kwargs.get('duration'))
        )
        keyUsage={
            'digital_signature': True, 
            'content_commitment':True, 
            'key_encipherment':True, 
            'data_encipherment':True, 
            'key_agreement':True, 
            'key_cert_sign':True, 
            'crl_sign':True,
            'encipher_only':True,
            'decipher_only':True 
        }
        extensions=[
            x509.SubjectKeyIdentifier.from_public_key(
                csr.public_key()),
            x509.KeyUsage(**keyUsage),
            x509.BasicConstraints(ca=True, path_length=None),
            x509.ExtendedKeyUsage([
                lib.x509.ObjectIdentifier(dotted_string='1.3.6.1.4.1.311.10.3.12'),
                lib.x509.ObjectIdentifier(dotted_string='1.2.840.113583.1.1.5'),
                lib.x509.ObjectIdentifier(dotted_string='1.3.6.1.4.1.311.20.2.2'),
                lib.x509.oid.ExtendedKeyUsageOID.EMAIL_PROTECTION,
                lib.x509.oid.ExtendedKeyUsageOID.CLIENT_AUTH,
                lib.x509.oid.ExtendedKeyUsageOID.SERVER_AUTH,
            ]),
            x509.AuthorityInformationAccess([
                lib.x509.AccessDescription(
                    lib.x509.oid.AuthorityInformationAccessOID.OCSP,
                    lib.x509.UniformResourceIdentifier('http://ocsp.e-mudhra.com')
                ),
                lib.x509.AccessDescription(
                    lib.x509.oid.AuthorityInformationAccessOID.CA_ISSUERS,
                    lib.x509.UniformResourceIdentifier('http://www.e-mudhra.com/repository/cacerts/C2ISCA2014.crt')
                ),
            ]),
            x509.CRLDistributionPoints([
                lib.x509.DistributionPoint(
                   full_name=[lib.x509.UniformResourceIdentifier(
                       'http://www.e-mudhra.com/repository/crls/C2ISCA2014.crl')], 
                   relative_name=None, 
                   reasons=None, 
                   crl_issuer=None
                ),
            ]),
            x509.CertificatePolicies([
                lib.x509.PolicyInformation(
                    lib.x509.ObjectIdentifier(dotted_string='2.16.356.100.2.2'),
                    [lib.x509.UserNotice(notice_reference=None, 
                                        explicit_text='Class 2 Certificate'),]
                    
                ),
                lib.x509.PolicyInformation(
                    lib.x509.ObjectIdentifier(dotted_string='2.16.356.100.1.8.2'),
                    ['CPS: http://www.e-mudhra.com/repository/cps/e-Mudhra_CPS.pdf',]
                    
                ),
            ])  
        ]
        for extension in extensions:
            cert=cert.add_extension(extension,critical=False)
        ski_ext = issuer_cert.extensions.\
                get_extension_for_class(x509.SubjectKeyIdentifier)
        extension=x509.AuthorityKeyIdentifier.\
                    from_issuer_subject_key_identifier(ski_ext.value)
        cert=cert.add_extension(extension,critical=False)
        self.csr=cert
        return self
    def sign_request(self,privateKeyFile,savePath,fileName='certificate.pem'):
        hashes=lib.hazmat.primitives.hashes
        key=privateKeyFile
        self.cert=self.csr.sign(key,hashes.SHA256())
        path=os.path.abspath(savePath)
        saveFile=path+'/'+fileName
        print(saveFile)
        serialization=lib.hazmat.primitives.serialization
        with open(saveFile, "wb") as f:
            f.write(self.cert.public_bytes(serialization.Encoding.PEM))
        return self

class CertificateConstructor:
    def loadKey(self,key):
        self.key=key
        return self
    def loadProps(self,props,**kwargs):
        for key in props.return_vals():
            setattr(self,key,getattr(props,key))
        self.subj_serial_number=base64.b16encode(os.urandom(24)).decode()
        self.pseudnoym=base64.b16encode(os.urandom(16)).decode()
        self.builderCls=kwargs.get('builderCls',
                                CertSignRequestBuilder)
        return self
    def new(self,builderCls,keyGenerate=False,**kwargs):
        if keyGenerate:
            self.key=builderCls().create_key_pair()
        csr=builderCls().create_certificate(**vars(self),
                                            publickey=self.key.public_key())
        cfy=Certify
        cert=cfy().signer_inputs(
            csr=csr,
            issuer_cert=kwargs.get('issuer'),
            duration=730,
        )
        cert=cert.sign_request(
            privateKeyFile=kwargs.get('issuerKey'),
            savePath=kwargs.get('savePath','.'),
            fileName=kwargs.get('fileName','certificate.pem'),
        )
        return cert.cert
    @classmethod
    def from_file(cls,filePath):
        with open(filePath,'rb') as data:
            cert=x509.load_pem_x509_certificate(data.read(), backend=None)
            return cert
    def save_to_file_pkcs12(self,pkcsFilenamePath,StorageName,**kwargs):
        if getattr(self,'key',None):
            fp=open(pkcsFilenamePath,'wb')
            blob=pkcs12.serialize_key_and_certificates(
                    name=StorageName.encode(),
                    key=self.key,
                    cert=self.new(builderCls=getattr(self,'builderCls',
                                                kwargs.get('builderCls')),
                                  keyGenerate=False,
                                  savePath=kwargs.get('savePath','.'),
                                  fileName=kwargs.get('fileName','certificate.pem'),
                                  issuer=kwargs.get('issuer'),
                                  issuerKey=kwargs.get('issuerKey'),
                                  ),
                    cas=None,
                    encryption_algorithm=lib.hazmat.primitives.serialization.NoEncryption(),
            )
            fp.write(blob)
            fp.close()
            print('file saved')
            return self
        raise Exception('Key does not exist')


if __name__=='__main__':
    issuerPath='Creds/keyStore.pem'
    savePath='NewCreds/'
    certName='certificate.pem'
    pkcsPath='NewCreds/secret.der'
    start=CertificateConstructor()
    props=CertificateProps.fromJson('NewCreds/certinfo.json')
    start.loadProps(props)
    #key=start.builderCls().create_key_pair()
    key=load_pem_private_key(open('NewCreds/private.pem','rb').read(),password=None)
    start.loadKey(key=key)
    issuer=CertificateConstructor.from_file('Creds/newcacert.pem')
    issuerKey=load_pem_private_key(open(issuerPath,'rb').read(),password=None)
    #following step is not required since directly saving to pkcs12
    #cert=start.new(start.builderCls,issuer=issuer,
    #                issuerKey=issuerKey,
    #                savePath=savePath,
    #                fileName=certName,
    #                )
    start.save_to_file_pkcs12(pkcsPath,
                            StorageName='trueFile',
                            issuerKey=issuerKey,
                            savePath=savePath,
                            fileName=certName,
                            issuer=issuer,
                                )

#help& references:
#1. https://oidref.com/2.5.29
#2. http://oid-info.com/get/2.16.356.100.1.8.2
#3. https://cryptography.io/en/latest/x509/tutorial/
#key conversion: 
#https://stackoverflow.com/questions/13732826/convert-pem-to-crt-and-key



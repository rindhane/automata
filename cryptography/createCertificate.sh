#! /usr/bin/env bash

python create_signerCertificate.py
echo 'create without password certifcate'
openssl pkcs12 -export -out NewCreds/certificatenopass.pfx -inkey NewCreds/private.pem -in NewCreds/certificate.pem
echo 'create certifcate with password'
openssl pkcs12 -export -out NewCreds/certificate.pfx -inkey NewCreds/private.pem -in NewCreds/certificate.pem
Procedures to transfer auth from Google Authenticator
===================================================

Following steps will provide the details to convert exported QR code from google authenticator to any device


Export QR code to uri
---------------------------------

Convert QR code from Google authenticator to uri by any QR code reader and the resultant string will look like `otpauth-migration://offline?data=Cko...........` .
The string in parameter `data` is required . 

This string contains encoded bytes in base64 encoding.
This string related to the `data` encoding will be used by protobuf to obtain the parameters out of it. 


**Utilizing Protobuf (Protocol Buffers)**
----------------------------------------

Firstly download the protoc compiler(or make from source) and then to convert `check.proto` to generate `check_pb2.py` file.

This `check_pb2.py` contains the class `MigrationPayload` (subclass of Message api) which will enable conversion from binary to python object class. 

Use file `uri_to_base32_secret.py`to utilize the `MigrationPayload` to complete the conversion. Present the string with parameter`data?=` to `data_string` variable to initiate the conversion. 


References: 
------------------------------
1. About usage of Protobuf in python `https://developers.google.com/protocol-buffers/docs/pythontutorial`

2. Post `https://alexbakker.me/post/parsing-google-auth-export-qr-code.html` by library `https://github.com/dim13/otpauth` made possible to convert binary to python object.
    1. Check out comments of this request `https://github.com/google/google-authenticator-android/issues/118`
    
3. Description of google authenticator process `https://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python`

4. Utilizing python lib for generating TOTP : `https://github.com/pyauth/pyotp`


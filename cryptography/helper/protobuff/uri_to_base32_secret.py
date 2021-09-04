import check_pb2
import base64
import pyotp

#inputs
data_string=#input here
object_no=0

#initiation of conversion
dataObject= check_pb2.MigrationPayload()
#populate data from data _string 
data=base64.b64decode(data_string)
dataObject.ParseFromString(data)

secret=dataObject.otp_parameters[object_no].secret
inputOTP=base64.b32encode(secret)
totp=pyotp.TOTP(inputOTP)
print(totp.now())

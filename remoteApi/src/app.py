#! /usr/bin/env python
import pprint
from flask import Flask,request
from mylogger import logger

app = Flask(__name__)

@app.route("/")
def hello_world():
    logger.info("hello_world")
    return "<h1>Hello, Welcome to the on-the-spot sms server.</h1>" 

@app.route("/sms",methods=["GET","POST"])
def print_sms():
    logger.info("print_sms")
    if request.is_json:
        pprint.pprint(request.get_json())
    else:
        data=dict(request.form) or dict(request.args)
        pprint.pprint(data)
    return ('Nothing',200)
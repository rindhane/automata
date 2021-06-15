from logging import FileHandler 
import logging
from flask import has_request_context, request

logger=logging.getLogger(__name__)

class RequestFormatter(logging.Formatter):
    def format(self,record):
        if has_request_context():
            record.url=request.url
            record.remote_addr=request.remote_addr
            record.path=request.path
            record.method=request.method
        else:
            record.url=None
            record.remote_addr=None
            record.path=None
            record.method=None
        
        return super().format(record)

formatter=RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s with path %(method)s %(path)s  \n'
    '%(name)s : %(levelname)s in %(module)s : %(message)s'
)

logFileHandler = FileHandler('alllogs.log')
logFileHandler.setFormatter(formatter)
logger.addHandler(logFileHandler)
logger.setLevel(logging.DEBUG)
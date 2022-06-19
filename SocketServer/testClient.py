#! /usr/bin/env python

import socket

def send_ping_data(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(b'Hello, world')
        data=s.recv(1024)
        return data
if __name__== "__main__" :
    print('Received',repr(send_ping_data('127.0.0.1','65432')))

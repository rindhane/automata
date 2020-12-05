#! /usr/bin/env python

import selectors
import socket

host=127.0.0.1
port = 65432
sel = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()
print('listening on >',(host,':',port))
lsock.setblocking(False)
sel.register(lsock,selectors.EVENT_READ, data='server')

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data == 'server':
            accept_wrapper(key.fileobj)
        else:
            service_connections(key,mask)

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('accepted connection from',addr)
    conn. setblocking(False)
    data= types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events=selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn,events, data=data)

def service_connection(key,mask):
    sock=key.fileobj
    data=key.data
    if mask & selectors.EVENT_READ :
        recv_data =sock.recv(1024)
        if recv_data :
            data.outb+= recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

#pending complete it with the help of following references:

https://realpython.com/python-sockets/
https://github.com/realpython/materials/tree/master/python-sockets-tutorial
https://chaobin.github.io/
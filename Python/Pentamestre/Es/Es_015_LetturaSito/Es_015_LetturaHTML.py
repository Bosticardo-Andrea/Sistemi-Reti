from http import client
import socket,sys
from urllib import response

from requests import request
target_host = "info.cern.ch"

target_port = 80
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
client.send(request.encode())
response = client.recv(512).decode()
s = ""
while len(response)>0:
    s += response[0]
    response = client.recv(512).decode()
k,ok = 0,True
while (k < len(s) and ok):
    if s[k:k+6] == "<html>": string = s[k:]
f = open("index.html","w")
f.write(s)
f.close()
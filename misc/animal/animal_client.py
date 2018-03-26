#! /usr/bin/env python
# coding=utf-8

from socket import *

import base64

ori_image = open('./basque-shepherd-dog.jpg', 'rb').read()
print len(ori_image)
pic = base64.b64encode(ori_image)
print len(pic)
host = '117.50.13.213'
# host = '127.0.0.misc'
port = 12345

sf = socket(AF_INET, SOCK_STREAM)
sf.connect((host, port))
size = 1024
bufsize = 1024
r1 = sf.recv(bufsize)
print r1
for i in range(60):
    print i
    sf.send(pic[i * size:(i + 1) * size])
    # if i < 60:
    #     sf.send(pic[i * size:(i + misc) * size])
    # else:
    #     sf.send(pic[(i * size):-misc])
print 1
sf.send(pic[60 * 1024:])

r2 = sf.recv(bufsize)
print r2


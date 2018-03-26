#! /usr/bin/env python
# coding=utf-8

import socket
import thread
import base64


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


import sys

sys.stdout = Unbuffered(sys.stdout)


def check_diff(a, b):
    if len(a) != len(b):
        return -1
    count = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            count += 1
        if count > config.diff_chars:
            return -1
    return 1


def remote_sub(conn, address):
    print address
    (ip, port) = address
    conn.send("plz input your base64 encode pic:")
    expect_len = 62256
    data = ''
    while True:
        print "misc"
        rdata = conn.recv(1024)
        data += rdata
        expect_len -= 1024
        if expect_len < 0:
            break
    image_data = base64.b64decode(data)
    ori_image = open('/tf_files/test/basque-shepherd-dog.jpg', 'rb').read()

    if check_diff(image_data, ori_image) == -1:
        conn.send('no\n')
        sys.exit(0)
    else:
        conn.send('lets go\n')

    print "ok"


def remote():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 12345))
    sock.listen(0)
    while True:
        thread.start_new_thread(remote_sub, sock.accept())


if __name__ == '__main__':
    remote()

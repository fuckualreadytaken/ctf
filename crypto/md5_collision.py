#! /usr/bin/env python
# coding=utf-8

import multiprocessing
import hashlib
import random
import string
import sys

CHARS = string.letters + string.digits


def cmp_md5(substr, stop_event, start=0, size=20):
    global CHARS
    while not stop_event.is_set():
        rnds = ''.join(random.choice(CHARS) for _ in range(size))
        md5 = hashlib.md5(rnds)
        if md5.hexdigest()[start:] == substr:
            print rnds
            stop_event.set()


if __name__ == '__main__':
    cpus = multiprocessing.cpu_count()
    stop_event = multiprocessing.Event()
    processes = [multiprocessing.Process(target=cmp_md5, args=("4d984a",
                                                               stop_event, -6))
                 for i in range(cpus)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
        # rnds = ''.join(random.choice(CHARS) for _ in range(10))
        # print rnds

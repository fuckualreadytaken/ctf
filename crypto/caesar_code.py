#! /usr/bin/env python
# coding=utf-8
words = "abcdefghijklmnopqrstuvwxyz"


def encrypto(key, message):
    cipher = ""
    for i in message:
        cipher += words[(words.index(i) + key) % 26]

    return cipher


def decrypto(key, cipher):
    message = ""
    for i in cipher:
        message += words[(words.index(i) - key) % 26]

    return message


if __name__ == "__main__":
    cipher = "dlsjvtlavjyfwav"
    print decrypto(7, cipher)

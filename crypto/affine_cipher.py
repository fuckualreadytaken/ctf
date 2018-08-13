#! /usr/bin/env python
# coding=utf-8

words = "abcdefghijklmnopqrstuvwxyz"


# def gcd(a, b):
#     # 辗转相除法求公因数，这里主要用于判断两数字是否互素
#     while a % b != 0:
#         y = a % b
#         a = b
#         b = y
#
#     return b


def egcd(a, b):
    # 扩展的欧几里得算法,这里主要用于判断是否互素和求逆元
    if b == 0:
        return 1, 0, a
    (x, y, r) = egcd(b, a % b)
    tmp = x
    x = y
    y = tmp - (a / b) * y
    return x, y, r


def invert(e, modulus):
    x, y, r = egcd(e, modulus)
    if r != 1:
        print "E and modulus is not coprime!"
        exit()
    if x < 0:
        x = x + modulus

    return x


def decrypto(k, b, cipher):
    message = ""
    k = invert(k, 26)
    print k
    for i in cipher:
        message += words[k * (words.index(i) - b) % 26]

    return message


def encrypto(k, b, message):
    cipher = ""
    for i in message:
        cipher += words[(words.index(i) * k + b) % 26]

    return cipher


if __name__ == "__main__":
    # m = "armmvxnzh"
    # print decrypto(3, 5, m)
    # 计算 φ
    f = 822 * 996
    d = invert(19, f)
    print d


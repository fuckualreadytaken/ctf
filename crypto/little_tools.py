#! /usr/bin/env python
# coding=utf-8
import sys


def input_int(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    try:
        n = int(raw_input())
        return n
    except:
        return 0


def egcd(a, b):
    if b == 0:
        return 1, 0, a
    (x, y, r) = egcd(b, a % b)
    tmp = x
    x = y
    y = tmp - (a / b) * y
    return x, y, r


def Invert():
    print "+" * 10 + "Invert" + "+" * 10
    print "Input your e (only number):"
    e = int(raw_input())
    print "Input your modulus (only number):"
    modulus = int(raw_input())
    x, y, r = egcd(e, modulus)
    if r != 1:
        print "E and modulus is not coprime!"
        exit()
    if x < 0:
        x = x + modulus

    print "The Invert result is %d" % x


def Railfence():
    print "+" * 10 + "Railfence" + "+" * 10
    print "Input your cipher:"
    e = raw_input()
    e = e.strip()
    print "Input your key:"
    key = int(raw_input())
    length = len(e)
    filling_bit = key - length % key
    num = length / key
    if filling_bit != 0:
        num += 1
        new_e = list(e)
        k = filling_bit
        while k > 0:
            new_e.insert(len(e) + filling_bit - (k - 1) * num - 1, " ")
            k -= 1
        e = ""
        for i in new_e:
            e += i

    i = 0
    result = ""
    while i < num:
        j = 0
        while j < key:
            result = result + e[i + j * num]
            j += 1
        i += 1
    print "Result : " + result.strip(" ")


def ModExp():
    print "+" * 10 + "ModExp" + "+" * 10
    print "Input your n (only number):"
    n = int(raw_input())
    print "Input your k (only number):"
    k = int(raw_input())
    print "Input your m (only number):"
    m = int(raw_input())
    a = list(bin(k))[2:]
    a.reverse()
    s = 1
    for i in a:
        if i == '1':
            s = (s * n) % m
        n = (n * n) % m
    print "The ModExp result is %d" % s


def menu():
    print "+" * 10 + "Welcome to little tools!" + "+" * 10
    while True:
        print "1. ModExp"
        print "2. Invert"
        print "3. Railfence"
        print "4. exit"
        sys.stdout.flush()
        choice = input_int("Command: ")
        {
            1: ModExp,
            2: Invert,
            3: Railfence,
            4: exit,
        }.get(choice, lambda *args: 1)()


if __name__ == "__main__":
    menu()

#! /usr/bin/env python
# -*-coding:utf-8-*-

# Author: ProofZ
# From: MD_labs

from factordb.factordb import FactorDB
import gmpy2
import rsa


def integer_factors(number):
    f = FactorDB(number)
    f.connect()
    return f.get_factor_list()


class RSA:
    def __init__(self, p=None, q=None, e=None, N=None, d=None, phi=None):
        """
        :param p: Prime p
        :param q: Prime q
        :param e: Security parameter e
        :param N: n = p*q
        :param d: SK
        :param phi: phi = (p - 1) * (q - 1)
        """
        self.p = p
        self.q = q
        self.e = e
        self.N = N
        self.d = d
        self.phi = phi
        if self.p is not None and self.q is not None:
            self.N = self.p * self.q
        if self.d is None:
            if self.phi is None:
                self.phi = (self.p - 1) * (self.q - 1)
            self.d = gmpy2.invert(self.e, self.phi)

    @staticmethod
    def ModExp(n, k, m):
        """This method is use to calculate the big Modular Exponentiation
        :param n: Base
        :param k: Component
        :param m: Modulus
        """
        a = list(bin(k))[2:]
        a.reverse()
        s = 1
        for i in a:
            if i == '1':
                s = (s * n) % m
            n = (n * n) % m
        return s

    def encrypto(self, m):
        """
        :param m: Plain text
        :return: Cipher text
        """

        return self.ModExp(m, self.e, self.N)

    def decrypto(self, c):
        """
        :param c: Cipher text
        :return: Plain text
        """
        return self.ModExp(c, self.d, self.N)

    @staticmethod
    def number2ascii(number):
        """
        :param number: Plain text
        :return: Ascii string of Plain text
        """
        h = hex(number)
        h = h[2:].strip("L")
        i = 0
        s = ""
        while i < len(h):
            s += chr(int(h[i:i + 2], 16))
            i += 2

        return s

    def decrypto_file(self, file_path):
        """
        :param file_path: file path
        :return: plain text
        """
        self.d = int(self.d)
        privatekey = rsa.PrivateKey(self.N, self.e, self.d, self.p, self.q)
        with open(file_path, "rb") as fp:
            return rsa.decrypt(fp.read(), privatekey).decode()


if __name__ == "__main__":
    e = 65537
    # n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
    # c = 0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d
    # d = 1
    # phi = 0x1564aade6f1b9f169dcc94c9787411984cd3878bcd6236c5ce00b4aad6ca7cb0ca8a0334d9fe0726f8b057c4412cfbff75967a91a370a1c1bd185212d46b581676cf750c05bbd349d3586e78b33477a9254f6155576573911d2356931b98fe4fec387da3e9680053e95a4709934289dc0bc5cdc2aa97ce62a6ca6ba25fca6ae366e86eed95d330ffad22705d24e20f9806ce501dda9768d860c8da465370fc70757227e729b9171b9402ead8275bf55d42000d51e16133fec3ba7393b1ced5024ab3e86b79b95ad061828861ebb71d35309559a179c6be8697f8a4f314c9e94c37cbbb46cef5879131958333897532fea4c4ecd24234d4260f54c4e37cb2db1a0
    p = 275127860351348928173285174381581152299
    q = 319576316814478949870590164193048041239
    r = RSA(e=e, p=p, q=q)
    file_path = "C:\\Users\\zpf\Desktop\\mediumrsa\\flag.enc"
    print r.decrypto_file(file_path)
    # print RSA.number2ascii(rsa.decrypto(c))

    # n = 0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
    # print integer_factors(int(n))

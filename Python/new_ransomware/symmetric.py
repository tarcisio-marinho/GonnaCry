#!/bin/bash/env python
# coding=UTF-8

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
# import generate_keys

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc, decryption_key=None):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        if(decryption_key):
            self.key = hashlib.sha256(decryption_key.encode()).digest()
            
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

# key = generate_keys.generate_key(32, True)
# a = AESCipher(key)

# enc = a.encrypt("TESTE CRYPTO")
# print(base64.b64decode(enc))

# back = a.decrypt(enc, key)

# print(back)
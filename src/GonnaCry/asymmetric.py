#!/bin/bash/env python
# coding=UTF-8
import os
from os import chmod
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

class assymetric():
    # Constructor
    def __init__(self):
        self.private_key_path = ""
        self.public_key_path = ""
        self.bit_len = 2048
        self.private_key_PEM = None
        self.public_key_PEM = None
        self.key = None


    def generate_keys(self):
        self.key = RSA.generate(self.bit_len)
        self.private_key_PEM = self.key.exportKey('OpenSSH')
        self.public_key_PEM = self.key.publickey().exportKey('OpenSSH')
        
    
    def encrypt(self, data):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.encrypt(data)


    def decrypt(self, data):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.decrypt(data)

    
    def save_to_file(self, path):
        self.private_key_path = os.path.join(path, "priv.key")
        self.public_key_path = os.path.join(path, "public.key")

        with open(self.private_key_path, 'w') as content_file:
            chmod(self.private_key_path, 600) # -rw------- permissions 
            content_file.write(self.private_key_PEM)

        with open(self.public_key_path, 'w') as content_file:
            content_file.write(self.public_key_PEM)


if __name__ == "__main__":
    cipher = assymetric()
    cipher.generate_keys()
    print(cipher.private_key_PEM)
    print(cipher.public_key_PEM)

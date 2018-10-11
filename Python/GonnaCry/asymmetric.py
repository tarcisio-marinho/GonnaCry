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


    # This function will generate RSA keys
    def generate_keys(self):
        self.key = RSA.generate(self.bit_len)
        self.private_key_PEM = self.key.exportKey('OpenSSH')
        self.public_key_PEM = self.key.publickey().exportKey('OpenSSH')
        
    
    def encrypt(self, data):
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(data)


    def decrypt(self, data):
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(data)

    
    def save_to_file(self, path):
        self.private_key_path = os.path.join(path, "priv.key")
        self.public_key_path = os.path.join(path, "public.key")

        with open(self.private_key_path, 'w') as content_file:
            chmod(self.private_key_path, 0600) # -rw------- permissions 
            content_file.write(self.private_key_PEM)

        with open(self.public_key_path, 'w') as content_file:
            content_file.write(self.public_key_PEM)

if __name__ == "__main__":
    msg = 'b180749119d72cc7eb33ea7e778aaad65eb868650497fa8c793785ecfa559e7d05ee2bfb29f8f5e40cfdd6a670b1db1701a0ca34c55a8298ed3edba01ede7658c1151a07797eca8be8b5ee7c263f5a2c52819b468fdb074cb4b3a61e47ee0926'
    a = assymetric()
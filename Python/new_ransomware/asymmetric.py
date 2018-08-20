#!/bin/bash/env python
# coding=UTF-8

from os import chmod
from Crypto.PublicKey import RSA

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
        self.private_key_PEM = self.key.exportKey('DER')
        self.public_key_PEM = self.key.publickey().exportKey('DER')
        
    
    def encrypt(self, data):
        return self.key.encrypt(data, 'x')[0]


    def decrypt(self, data):
        return self.key.decrypt(data)

    
    def save_to_file(self, path):
        self.private_key_path = path + "priv.key"
        self.public_key_path = path + "public.key"

        with open(self.private_key_path, 'w') as content_file:
            chmod(self.private_key_path, 0600) # -rw------- permissions 
            content_file.write(self.private_key_PEM)

        with open(self.public_key_path, 'w') as content_file:
            content_file.write(self.public_key_PEM)


if __name__ == "__main__":
    a = assymetric()
    a.generate_keys()
    enc = a.encrypt("ola tudo bem? ")
    print(enc)
    print(a.decrypt(enc))
    a.save_to_file("./")
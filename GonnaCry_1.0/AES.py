#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
# got from here: http://stackoverflow.com/questions/16761458/how-to-aes-encrypt-decrypt-files-using-python-pycrypto-in-an-openssl-compatible
from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random
import os
import string
import random

def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = ''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]

# criptografa o arquivo, criando novo arquivo com uma senha AES.
def encrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = Random.new().read(bs - len('Salted__'))
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_file.write('Salted__' + salt)
    finished = False
    while not finished:
        chunk = in_file.read(1024 * bs)
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += padding_length * chr(padding_length)
            finished = True
        out_file.write(cipher.encrypt(chunk))

# got from here: https://ubuntuforums.org/showthread.php?t=2299355
def generate_data(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

# destroi o arquivo original e depois exclui, não podendo recupera-lo com buscas na memória
def shred(file_name,  passes):
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

# chama a função encrypt. criptografa e remove o arquivo
def criptografa(senha,caminho_arquivo):
    print('Encrypting ~> '+ caminho_arquivo)
    with open(caminho_arquivo, 'rb') as in_file, open(caminho_arquivo+'.cripto', 'wb') as out_file:
        encrypt(in_file, out_file, senha)
    shred(caminho_arquivo,1) # deixa o arquivo ilegível e depois o deleta

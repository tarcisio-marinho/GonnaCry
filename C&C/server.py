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
    sc, address = s.accept()

    f = open ("teste.txt", "rb")
    l = f.read(1024)
    while (l):
        sc.send(l)
        l = f.read(1024)
    s.close()



# NÃO RODE ESTE CÓDIGO #
# AS CHAVES JA FORAM GERADAS, E DEVEM PERMANECER ÚNICAS
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
conexao('localhost')

#conexao('127.0.0.1')

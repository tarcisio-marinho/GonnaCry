#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import subprocess, random, socket

from Crypto.PublicKey import RSA
import os

def conexao(meuIP):
    # servidor
    f=open('private_key.txt','r')
    chave_privada=f.read()
    print(chave_privada)
    print('Servidor rodando')
    while True:
        porta=6064

        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
        socket_obj.bind((meuIP, porta))
        socket_obj.listen(1) # escuta apenas 1 "vitma"
        #os.system('clear')
        conexao,endereco=socket_obj.accept()

        # ao se conectar, envia a chave privada (S)
        conexao.send(str(chave_privada))
        # recebeu do cliente o ID

        print(recebido)

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




gera_chaves()

#conexao('127.0.0.1')

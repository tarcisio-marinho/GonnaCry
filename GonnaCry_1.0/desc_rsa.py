from Crypto.PublicKey import RSA
import os
def RSA_to_AES():
    file_enc='keys/AES.txt.enc'
    novo='keys/AES.txt'
    file_priv='keys/chave_privada_cliente.txt'
    f=open(file_priv,'rb')
    chave_privada=f.read()
    f.close()
    f=open(file_enc,'rb')
    dados=f.read()
    f.close()
    chave_privada_obj=RSA.importKey(chave_privada)
    dados_dec=chave_privada_obj.decrypt(dados)
    f=open(novo,'w')
    f.write(dados_dec)
    f.close()
    os.remove(file_enc)

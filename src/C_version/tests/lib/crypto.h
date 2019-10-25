#ifndef CRYPTO
#define CRYPTO

#include"struct.h"
#include<stdio.h>

void encrypt_files(List *files, List **encrypted, List **not_encrypted);
void decrypt_files(List *encrypted);
void shred(char *path);
void encrypt(FILE *in, FILE *out, char *key, char *iv);
void decrypt(FILE *in, FILE *out, char *key, char *iv);


#endif

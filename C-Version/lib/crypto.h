#ifndef CRYPTO
#define CRYPTO

#include"struct.h"
#include<stdio.h>

void encrypt_files(List *files, EncList **encrypted, List **not_encrypted);
void encrypt(FILE *in, FILE *out, char *key, char *iv);
void decrypt(FILE *in, FILE *out, char *key, char *iv);


#endif

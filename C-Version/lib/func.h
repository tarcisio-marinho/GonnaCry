
#ifndef FUNC
#define FUNC

#include<stdio.h>
#include "struct.h" 
void find_files(List **files, char* start_path);
void save_into_file_encrypted_list(EncList *l, char * start_path);
void read_from_file_encrypted_files(EncList **l, char * start_path);
void encrypt_files(List *files, EncList **encrypted, List **not_encrypted);
void encrypt(FILE *in, FILE *out, char *key, char *iv);
void decrypt(FILE *in, FILE *out, char *key, char *iv);
const char *get_filename_ext(const char *filename);
char * generate_key(int length);
#endif
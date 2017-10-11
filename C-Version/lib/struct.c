#include"struct.h"
#include<stdlib.h>
#include<string.h>
#include<stdio.h>

/**
 * This function will append the path to the l(List).
 * It's a simple Linked List.
 * @param l -> type = List
 * @param file_path -> type = char * (String)
 */
void append(List **l, char *file_path){
    List *aux = NULL;
    int len = strlen (file_path);
    aux = (List*)malloc(sizeof(List));
    aux->path = (char*)malloc(sizeof(char)* (len+1));
    strcpy(aux->path, file_path);
    
    /*Linked List*/
    if(*l == NULL){
        (*l) = aux;
        (*l)->prox = NULL;
    }else{
        aux->prox = *l;
        (*l) = aux;
    }
}

/**
 * This function will append the path, key and iv in the l(EncList).
 * It's a simple Linked List.
 * @param l -> type = EncList
 * @param file_path -> type = char * (String)
 * @param key -> type = char * (String)
 * @param iv -> type = char * (String)
 */
void append_encrypted(EncList **l, char *file_path, char *key, char *iv){
    EncList *aux = NULL;
    int len = strlen (file_path);
    int key_len = strlen(key);
    int iv_len = strlen(iv);
    
    aux = (EncList*)malloc(sizeof(EncList));
    aux->path = (char*)malloc(sizeof(char)* (len+1));
    aux->iv = (char*)malloc(sizeof(char)*(iv_len +1));
    aux->key = (char*)malloc(sizeof(char) * (key_len+1));
    
    strcpy(aux->path, file_path);
    strcpy(aux->iv, iv);
    strcpy(aux->key, key);
    
    /*Linked List*/
    if(*l == NULL){
        (*l) = aux;
        (*l)->prox = NULL;
    }else{
        aux->prox = *l;
        (*l) = aux;
    }
}

/**
 * This function destroys the l(List).
 * releasing the memory with free().
 * @param l -> type = List
 */
void destroy(List **l){
    List *aux;
    while(*l != NULL){
        aux = *l;
        *l = aux->prox;
        free(aux);
    }
}

/**
 * This function destroys the l(EncList)
 * releasing the memory with free().
 * @param l -> type = EncList
 */
void destroy_encrypted_list(EncList **l){
    EncList *aux;
    while(*l != NULL){
        aux = *l;
        *l = aux->prox;
        free(aux);
    }
}

/**
 * This function print all the path's of the l(List), only used for debugging.
 * @param l -> type = List
 */
void print(List *l){
    while(l != NULL){
        printf("%s\n", l->path);
        l = l->prox;
    }
}

/**
 * This function print all the path's, key's and iv's of the l(EncList), 
 * only used for debugging.
 * @param l -> type = EncList
 */
void print_encrypted_list(EncList *l){
    while(l != NULL){
        printf("{'key': '%s', 'iv':'%s', 'path':'%s'}\n", l->key, l->iv, l->path);
        l = l->prox;
    }
}

/**
 * This function return the length of the l(List).
 * @param l -> type = List
 * @return -> type = int
 */
int length(List *l){
    int len = 0;
    while(l != NULL){
        l = l->prox;
        len++;
    }
    return len;
}

/**
 * This function return the length of the l(EncList).
 * @param l -> type = EncList
 * @return -> type = int
 */
int length_encrypted_list(EncList *l){
    int len = 0;
    while(l != NULL){
        l = l->prox;
        len++;
    }
    return len;
}

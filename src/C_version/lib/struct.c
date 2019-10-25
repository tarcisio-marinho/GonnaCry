#include"struct.h"
#include<stdlib.h>
#include<string.h>
#include<stdio.h>

/**
 * This function will append the path, key and iv to the l(List).
 * It's a simple Linked List.
 * @param l -> type = List
 * @param file_path -> type = char * (String)
 */
void append(List **l, char *file_path, char *key, char *iv){
    List *aux = NULL;
    

    if(key == NULL && iv == NULL){
        int len = strlen (file_path);
        aux = (List*)malloc(sizeof(List));
        aux->info[2] = (char*)malloc(sizeof(char)* (len+1));
        strcpy(aux->info[2], file_path);

    }else{
        int len = strlen (file_path);
        aux = (List*)malloc(sizeof(List));
        aux->info[0] = (char *)malloc(sizeof(char) * 33);
        aux->info[1] = (char *)malloc(sizeof(char) * 17);
        aux->info[2] = (char *)malloc(sizeof(char) * (len+1));
        strcpy(aux->info[0], key);
        strcpy(aux->info[1], iv);
        strcpy(aux->info[2], file_path);
    }

    /*Linked List*/
    if(*l == NULL){
        (*l)->size = 0;
        (*l) = aux;
        (*l)->prox = NULL;
    }else{
        aux->prox = *l;
        (*l) = aux;
    }

    // Increment the size of the list
    (*l)->size++;
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
        
        // Clean the keys
        for(int i; i < 3; i++){
            // overwrite old memory
            *aux->info[i] = "random_string";
            free(aux->info[i]);
        }

        free(aux);
    }
}


/**
 * This function print all the path's, key's and iv's of the l(List), only used for debugging.
 * @param l -> type = List
 */
void print(List *l){
    while(l != NULL){
        
        if(!l->info[0])    printf("%s\n", l->info[2]);
        else   printf("KEY = %s IV = %s PATH = %s\n", l->info[0], l->info[1], l->info[2]);
        
        l = l->prox;
        
    }
}

/**
 * This function return the length of the l(List).
 * @param l -> type = List
 * @return -> type = integer
 */
int length(List *l){
    return l->size;
}

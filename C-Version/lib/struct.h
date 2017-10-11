#ifndef STRUCTS
#define STRUCTS

typedef struct node{
    struct node *prox;
    char *path;
}List;

typedef struct encryptedNode{
    struct encryptedNode *prox;
    char *path;
    char *key;
    char *iv;
}EncList;

void append(List **l, char *file_path);
void append_encrypted(EncList **l, char *file_path, char *key, char *iv);
void destroy(List **l);
void destroy_encrypted_list(EncList **l);
void print(List *l);
void print_encrypted_list(EncList *l);
int length(List *l);
int length_encrypted_list(EncList *l);
#endif

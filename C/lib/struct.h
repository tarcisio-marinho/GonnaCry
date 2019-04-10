#ifndef STRUCTS
#define STRUCTS


/**
 * info[0] = key
 * info[1] = iv
 * info[2] = path
 */
typedef struct node{
    struct node *prox;
    char * info[3];
    int size;
}List;

void append(List **l, char *file_path, char *key, char *iv);
void destroy(List **l);
void print(List *l);
int length(List *l);
#endif

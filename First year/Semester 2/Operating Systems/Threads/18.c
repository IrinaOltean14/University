// Create a C program that converts all lowecase letters from the command line arguments to uppercase 
// letters and prints the result. Use a thread for each given argument.
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <string.h>

typedef struct{
        char* word;
        int n;
}data;
pthread_mutex_t m;

void* f(void* arg){
        data p = *(data*) arg;
        int d = 'a'-'A';
//      printf("%d\n", p.n);
        for (int i = 0; i < p.n; i++){
//              printf("%c ", p.word[i]);
                if (p.word[i] >= 'a' && p.word[i] <= 'z'){
                        pthread_mutex_lock(&m);
                        p.word[i]-=d;
                        pthread_mutex_unlock(&m);
                }
        }

        return NULL;
}

int main(int argc, char** argv){

        pthread_t th[argc];
        data p[argc];
        pthread_mutex_init(&m, NULL);
        for (int i = 1; i < argc; i++){
//              printf("%s\n", argv[i]);
                p[i].word = argv[i];
                p[i].n = strlen(argv[i]);
                pthread_create(&th[i-1], NULL, f, (void*)&p[i]);
        }

        for (int i = 1; i < argc; i++){
                pthread_join(th[i-1], NULL);
        }

        pthread_mutex_destroy(&m);
//      printf("GATA");
        for (int i = 1; i < argc; i++){
                printf("%s\n", argv[i]);
        }
        return 0;
}

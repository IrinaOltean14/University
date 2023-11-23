// Write a program that receives strings of characters as command line arguments. For each string 
// the program creates a thread which calculates the number of digits, the number of leters and the 
// number of special characters (anything other than a letter or digit). The main program waits for 
// the threads to terminate and prints the total results (total number of digits, letters and special 
// characters across all the received command line arguments) and terminates. Use efficient 
// synchronization. Do not use global variables

#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <string.h>

typedef struct{
        char* word;
        int len;
        int* letters;
        int* digits;
        int* special;
        pthread_mutex_t* mutex;
}data;

void* f(void* arg){
        data p = *(data*)arg;
        for (int i = 0; i < p.len; i++){
                if (p.word[i] >= 'a' && p.word[i] <= 'z'){
                        pthread_mutex_lock(&p.mutex[0]);
                        (*p.letters)++;
                        pthread_mutex_unlock(&p.mutex[0]);
                }
                else if (p.word[i] >= '0' && p.word[i] <= '9'){
                        (*p.digits)++;
                }
                else{
                        (*p.special)++;
                }
        }
        return NULL;
}

int main(int argc, char** argv){

        pthread_t th[argc];
        data p[argc];
        int letters = 0, digits = 0, special = 0;
        pthread_mutex_t mutex[3];
        for (int i = 0; i < 3; i++){
                pthread_mutex_init(&mutex[i], NULL);
        }
        for (int i = 1; i < argc; i++){
                p[i].word = argv[i];
                p[i].len = strlen(argv[i]);
                p[i].letters = &letters;
                p[i].digits = &digits;
                p[i].special = &special;
                p[i].mutex = mutex;
                pthread_create(&th[i-1], NULL, f, (void*)&p[i]);
        }
        for (int i = 0; i < 3; i++){
                pthread_mutex_destroy(&mutex[i]);
        }

        for (int i = 1; i < argc; i++)
                pthread_join(th[i-1], NULL);

        printf("Letters: %d\n", letters);
        printf("Digits: %d\n", digits);
        printf("Others: %d\n", special);
        return 0;
}

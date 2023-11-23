 // Write a C program that receives integers as command line argument. The program will keep a 
// frequency vector for all digits. The program will create a thread for each argument that counts 
// the number of occurences of each digit and adds the result to the frequency vector. 
// Use efficient synchronization.

#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

int v[10];
pthread_mutex_t mutex;

void* f(void* arg){
        int x = *(int*)arg;
        while (x!=0){
                int digit = x % 10;
                pthread_mutex_lock(&mutex);
                v[digit]++;
                pthread_mutex_unlock(&mutex);
                x = x / 10;
        }
        return NULL;
}

int main(int argc, char** argv){

        pthread_t th[argc];
        int p[argc];
        pthread_mutex_init(&mutex, NULL);

        for (int i = 0; i < argc-1; i++){
                p[i] = atoi(argv[i+1]);
                pthread_create(&th[i], NULL, f, (void*)&p[i]);
        }

        for (int i = 0; i < argc-1; i++){
                pthread_join(th[i], NULL);
        }

        for (int i = 0; i < 10; i++){
                printf("v[%d] = %d\n", i, v[i]);
        }

        pthread_mutex_destroy(&mutex);
        return 0;
}

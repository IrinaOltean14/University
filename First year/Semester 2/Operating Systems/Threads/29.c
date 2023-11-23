//Write a C program that reads a number n from standard input and creates n threads, numbered from 0 to n - 1. Each thread places a random number between 10 and 20 on the position indicated by its id in an array of integers. After all threads have placed their number in the array, each thread repeats the following:
// - Checks if the number on its own position is greater than 0.
// - If yes, it substracts 1 from all numbers of the array, except the one on its own position.
// - If not, the thread terminates.
// - If there are no numbers in the array that are greater than 0, except the number on the thread's index position, the thread terminates.
// After all threads terminate, the main process prints the array of integers. Use appropriate synchronization mechanisms.


#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

pthread_barrier_t b;
pthread_mutex_t m;
typedef struct{
        int* a;
        int id;
        int n;
}data;

void* f(void* arg){
        data p = *(data*)arg;
        int x = random() % 3;
        p.a[p.id] = x;
        int ok = 1, greater;
        int ceva = 1;
        pthread_barrier_wait(&b);
        while (ok){
                pthread_mutex_lock(&m);
                if (p.a[p.id] <= 0)
                        break;
                greater = 0;
                printf("Before Id: %d\n", p.id);
                for (int i = 0; i < p.n; i++)
                        printf("%d ", p.a[i]);
                printf("\n");
                for (int i = 0; i < p.n; i++){
                        if (i != p.id && p.a[i] > 0){
                                p.a[i]--;
                                greater = 1;
                        }
                }

                printf("After Id: %d\n", p.id);
                for (int i = 0; i < p.n; i++)
                        printf("%d ", p.a[i]);
                printf("\n");
                pthread_mutex_unlock(&m);
                if (greater == 0){
                        ceva = 2;
                        break;
                }

        }
        pthread_mutex_unlock(&m);
        return NULL;
}

int main(int argc, char** argv){

        printf("N= ");
        int n;
        scanf("%d", &n);
        int a[n];
        pthread_t th[n];
        pthread_barrier_init(&b, NULL, n);
        pthread_mutex_init(&m, NULL);
        data p[n];
        for (int i = 0; i < n; i++){
                p[i].id = i;
                p[i].a = a;
                p[i].n = n;
                pthread_create(&th[i], NULL, f, (void*)&p[i]);
        }

        for (int i = 0; i < n; i++){
                pthread_join(th[i], NULL);
        }
        pthread_barrier_destroy(&b);
        pthread_mutex_destroy(&m);
        for (int i = 0; i < n ; i++)
                printf("v[%d] = %d\n", i, a[i]);

        return 0;
}

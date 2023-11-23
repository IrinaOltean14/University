// calculate the sum of all the elements of the matrix using as many threads as there are rows, 
// each thread adds to the total the numbers on a row.

#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mutex;
int totalSum;

typedef struct{
        int columns;
        int* row;
}data;

void* f(void* arg){

        data p = *(data*)arg;
        int sum = 0;
        for (int i = 0; i < p.columns; i++){
                //pthread_mutex_lock(&mutex);
                sum+=p.row[i];
                //pthread_mutex_unlock(&mutex);
        }
        pthread_mutex_lock(&mutex);
        totalSum += sum;
        pthread_mutex_unlock(&mutex);
//      printf("%d\n", sum);
        return NULL;
}

int main(int argc, char** argv){

        // Read the matrix from the file
        FILE* file;
        file = fopen("file.txt", "r");
        int rows, columns;
        if (file == NULL){
                printf("Failed to open file\n");
                return 1;
        }
        pthread_mutex_init(&mutex, NULL);
        fscanf(file, "%d", &rows);
        fscanf(file, "%d", &columns);
        int matrix[rows][columns];
        for (int i = 0; i < rows; i++)
                for (int j = 0; j < columns; j++)
                        fscanf(file, "%d", &matrix[i][j]);
        data v[rows];
        pthread_t th[rows];
        for (int i = 0; i < rows; i++){
                v[i].row = matrix[i];
                v[i].columns = columns;
                pthread_create(&th[i], NULL, f, (void*)&v[i]);
        }
        for (int i = 0; i < rows; i++){
                pthread_join(th[i], NULL);
        }
        pthread_mutex_destroy(&mutex);
        printf("The total sum is: %d\n", totalSum);
        return 0;
}

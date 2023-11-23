#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h>
//Folosind canale PIPE implementati urmatorul scenariu:
//Procesul A citeste N intregi de la tastatura si ii trimite unui proces numit B. Procesul B va
// adauga un numar aleator, intre 2 si 5, la toate numerele primite de la procesul A si le va trimite
//unui alt proces numit C. Procesul C va adauga toate numerele primite si va trimite suma inapoi procesului A. Toate procesele vor afisa un mesaj cu numerele primite si trimise.

int main(int argc, char** argv){

        int n;
        int v[100];
        int a2b[2];
        int b2c[2];
        int c2a[2];
        pipe(a2b);
        pipe(b2c);
        pipe(c2a);
        int pid1 = fork();
        if (pid1 == 0){
                // B
                close(a2b[1]);
                close(b2c[0]);
                close(c2a[0]);
                close(c2a[1]);
                read(a2b[0], &n, sizeof(int));
                for (int i =0; i<n; i++){
                        read(a2b[0], &v[i], sizeof(int));
                        //printf("%d\n", v[i]);
                        int x = rand() % 4;
                        x += 2;
                        v[i] += x;
                }
                write(b2c[1], &n, sizeof(int));
                for (int i=0; i<n; i++){
                        write(b2c[1], &v[i], sizeof(int));
                }
                close(b2c[1]);
                close(a2b[0]);
                exit(0);
        }

        int pid2 = fork();
        if (pid2 == 0){
                //C
                close(b2c[1]);
                close(c2a[0]);
                int sum=0;
                read(b2c[0], &n, sizeof(int));
                for (int i=0; i<n; i++){
                        read(b2c[0], &v[i], sizeof(int));
                        sum+=v[i];
                }
                write(c2a[1], &sum, sizeof(int));
                close(c2a[1]);
                close(b2c[0]);
                close(a2b[0]);
                close(a2b[1]);
                exit(0);
        }
        //A
        close(a2b[0]);
        close(b2c[0]);
        close(b2c[1]);
        close(c2a[1]);
        printf("Enter n: ");
        scanf("%d", &n);
        for (int i=0; i<n; i++){
                printf("v[%d]=", i);
                scanf("%d", &v[i]);
        }
        write(a2b[1], &n, sizeof(int));
        for (int i=0; i<n; i++){
                write(a2b[1], &v[i], sizeof(int));
        }
        int sum;
        read(c2a[0], &sum, sizeof(int));
        printf("Sum: %d\n", sum);
        close(a2b[1]);
        close(c2a[0]);
        wait(0);
        wait(0);
        return 0;

}

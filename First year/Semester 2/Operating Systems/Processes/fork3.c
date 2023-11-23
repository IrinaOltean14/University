#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
// Scrieti un program C (numit A) care creeaza un proces fiu B. Procesul B genereaza un numar aleator intre 100 si 1000. Procesul A genereaza cate un numar aleator intre 50 si 1050 si il trimite
// procesului B pana cand diferenta absoluta intre numarul generat de B si numarul trimis de A este mai mica decat 50. B afiseaza fiecare numar primit de la A. A va afisa la final numarul de numere
// generate pana cand conditia de oprire este indeplinita.

int main(int argc, char** argv){
        srand(time(NULL));
        int a2b[2];
        pipe(a2b);
        int b2a[2];
        pipe(b2a);
        int pid = fork();
        if (pid == 0){
                // in B
                close(a2b[1]);
                close(b2a[0]);

                int n, m;
                n = rand() % 901;
                n+=100;
                printf("B: n=%d\n", n);
                while(1){
                        if (read(a2b[0], &m, sizeof(int)) <=0){
                                break;
                        }
                        printf("B: %d\n", m);
                        int d = m-n;
                        if (d<1){
                                d=d*(-1);
                        }
                        printf("D=%d\n", d);
                        int found = 0;
                        if (d<50){
                                found=1;
                        }
                        write(b2a[1], &found, sizeof(int));
                }

                close(b2a[1]);
                close(a2b[0]);
                exit(0);
        }
        close(a2b[0]);
        close(b2a[1]);
        int count = 0;
        while(1){
                int n;
                count++;
                n=rand() % 1001;
                n+=50;
                write(a2b[1], &n, sizeof(int));
                int found;
                read(b2a[0], &found, sizeof(int));
                if (found==1){
                        printf("FOUND %d\n", count);
                        break;
                }
        }

        close(b2a[0]);
        close(a2b[1]);
        wait(0);
        return 0;
}

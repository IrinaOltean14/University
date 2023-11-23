#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char** argv){
        int pid2, pid1;
        int n;
        int a2b[2], b2p[2], p2a[2];
        pipe(a2b);
        pipe(b2p);
        pipe(p2a);
        pid1=fork();
        if (pid1==0){
                close(a2b[0]);
                close(b2p[0]);
                close(b2p[1]);
                close(p2a[1]);
                while(1){
                        if (read(p2a[0], &n, sizeof(int))<=0)
                                break;
                        if (n==0)
                                break;
                        n--;
                        printf("A: %d \n", n);
                        write(a2b[1], &n, sizeof(int));
                }
                close(a2b[1]);
                close(p2a[0]);
                exit(0);
        }
        else{
                pid2=fork();
                if (pid2==0){
                        close(p2a[0]);
                        close(p2a[1]);
                        close(a2b[1]);
                        close(b2p[0]);
                        while(1){
                                if (read(a2b[0], &n, sizeof(int)) <=0)
                                        break;
                                if (n==0)
                                        break;
                                n--;
                                printf("B: %d\n", n);
                                write(b2p[1], &n, sizeof(int));
                        }
                        close(b2p[1]);
                        close(a2b[0]);
                        exit(0);
                }
                n=10;
                close(a2b[0]);
                close(a2b[1]);
                close(p2a[0]);
                while(1){
                        if (read(b2p[0], &n, sizeof(int)) <=0)
                                break;
                        if (n==0)
                                break;
                        n--;
                        printf("P:%d\n", n);
                        write(p2a[1], &n, sizeof(int));
                }
                close(b2p[0]);
                close(p2a[1]);
                wait(NULL);
                wait(NULL);
        }

        return 0;
}

#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
// Un proces parinte cu doi copii. Parintele citeste cuvinte pana se citeste 'X'. Trimite cuvintele la copilul A care face un vector de frecventa pt numere. Copilul a trimite vectorul de frecventa la parinte
// si parintele afiseaza vectorul. CA trimite vectorul la CB si B calculeaza suma cifrelor si o afiseaza.

int main(int argc, char** argv){

        int p2a[2];
        int a2b[2];
        int a2p[2];
        pipe(a2p);
        pipe(a2b);
        pipe(p2a);
        int pid1 = fork();

        if (pid1 == 0){
                // in child 1 / A
                close(p2a[1]);
                close(a2p[0]);
                close(a2b[0]);
                char word[100];
                int v[12] = {0};
                int n=10;
                write(a2p[1], &n, sizeof(int));
                while(1){
                        if (read(p2a[0], word, sizeof(word)) <= 0){
                                break;
                        }
                        for (int i=0; i<strlen(word); i++){
                                if (word[i] >= '0' && word[i] <= '9'){
                                        int digit = word[i] - '0';
                                        v[digit] = v[digit]+1;
                                }

                                else{
                                        v[10] = v[10] + 1;
                                }
                        }
                }
                // passing the vector of numbers to the parent
                for (int i = 0;i<=10; i++){
                        write(a2b[1], &v[i], sizeof(int));
                }
                close(a2b[1]);
                close(a2p[1]);
                close(p2a[0]);
                exit(0);
        }

        int pid2 = fork();
        if (pid2 == 0){
                // in child 2 /B
                close(p2a[0]);
                close(p2a[1]);
                close(a2b[1]);
                close(a2p[0]);
                close(a2p[1]);
                int v[12];
                for (int i =0; i<=10;i++){
                        read(a2b[0], &v[i], sizeof(int));
                        printf("v[%d]=%d\n", i, v[i]);
                }
        //      close(a2p[1]);
                close(a2b[0]);
                exit(0);
        }
        // citire cuvinte de la tastatura
        close(p2a[0]);
        close(a2b[1]);
        close(a2b[0]);
        close(a2p[1]);
        while(1){
                char word[100];
                printf("Introdu cuvant: ");
                scanf("%s", word);
                //printf("%s\n",word);
                if (strcmp(word, "X")==0){
                        break;
                }
                write(p2a[1], word, strlen(word)+1);
        }

        int n;
        read(a2p[0], &n, sizeof(int));
        close(a2p[0]);
        close(p2a[1]);
        wait(0);
        wait(0);

        return 0;
}

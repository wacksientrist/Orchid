#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
    while (1) {
        FILE *file;
        file = fopen("Instrc_n.txt", "r");
        char content[10];
        fgets(content, 10, file);

        if (strcmp(content, "n\n") == 0) {
            fclose(file);
            usleep(100000);

            FILE *fil1, *fil2;
            fil1 = fopen("Instrc_r.txt", "r");
            fil2 = fopen("Instrc_s.txt", "w");

            char str[100], *token;
            fgets(str, 100, fil1);

            token = strtok(str, "!!!!!!!");
            float A = atof(token);
            token = strtok(NULL, "!!!!!!!");
            float B = atof(token);
            token = strtok(NULL, "!!!!!!!");
            char *Type = token;

            float Out;
            if (strcmp(Type, "A") == 0) {
                Out = A + B;
            }
            else if (strcmp(Type, "S") == 0) {
                Out = A - B;
            }
            else if (strcmp(Type, "M") == 0) {
                Out = A * B;
            }
            else if (strcmp(Type, "D") == 0) {
                Out = A / B;
            }
            else if (strcmp(Type, "IF=") == 0) {
                if (A == B) {
                    Out = 'T';
                }
                else {
                    Out = 'F';
                }
            }
            else if (strcmp(Type, "IF!") == 0) {
                if (A == B) {
                    Out = 'F';
                }
                else {
                    Out = 'T';
                }
            }
            else if (strcmp(Type, "IF>") == 0) {
                if (A > B) {
                    Out = 'T';
                }
                else {
                    Out = 'F';
                }
            }
            else if (strcmp(Type, "IF<") == 0) {
                if (A < B) {
                    Out = 'T';
                }
                else {
                    Out = 'F';
                }
            }
            char Out1[6];
            gcvt(Out, 6, Out1);
            fprintf(fil2, "%s", Out1);
            fclose(fil1);
            fclose(fil2);
        }
        else {
            fclose(file);
        }
    }
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    FILE *A_fil = fopen("Instrc_r1.txt", "r");
    FILE *B_fil = fopen("Instrc_r2.txt", "r");
    FILE *Type_fil = fopen("Instrc_r3.txt", "r");
    FILE *O_fil = fopen("Instrc_s.txt", "w");

    char A_char[5];
    char B_char[5];
    char Type_char[5];
    char O_char[5];

    double A_Float;
    double B_Float;
    double O_Float;

    fgets(Type_char, 4, Type_fil);

    if (strcmp(Type_char, "IF=") == 0)
    {
        fgets(A_char, 4, A_fil);
        fgets(B_char, 4, B_fil);

        if (strcmp(A_char, B_char) == 0)
        {
            strcpy(O_char, "T");
        }
        else
        {
            strcpy(O_char, "F");
        }
    }
    if (strcmp(Type_char, "IF!") == 0)
    {
        fgets(A_char, 4, A_fil);
        fgets(B_char, 4, B_fil);

        if (strcmp(A_char, B_char) == 0)
        {
            strcpy(O_char, "F");
        }
        else
        {
            strcpy(O_char, "T");
        }
    }
    if (strcmp(Type_char, "A") == 0)
    {
        fgets(A_char, 4, A_fil);
        fgets(B_char, 4, B_fil);

        A_Float = atof(A_char);
        B_Float = atof(B_char);

        gcvt((A_Float + B_Float), 4, O_char);
    }
    if (strcmp(Type_char, "S") == 0)
    {
        fgets(A_char, 4, A_fil);
        fgets(B_char, 4, B_fil);

        A_Float = atof(A_char);
        B_Float = atof(B_char);

        gcvt((A_Float - B_Float), 4, O_char);
    }
    if (strcmp(Type_char, "M") == 0)
    {
        fgets(A_char, 4, A_fil);
        fgets(B_char, 4, B_fil);

        A_Float = atof(A_char);
        B_Float = atof(B_char);

        gcvt((A_Float * B_Float), 4, O_char);
    }
    if (strcmp(Type_char, "D") == 0)
    {
        fgets(A_char, 4, A_fil);
        fgets(B_char, 4, B_fil);

        A_Float = atof(A_char);
        B_Float = atof(B_char);

        gcvt((A_Float / B_Float), 4, O_char);
    }
    fprintf(O_fil, "%s",O_char);

    return 0;
}
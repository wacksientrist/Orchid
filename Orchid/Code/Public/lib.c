#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 1024

typedef struct Instance {
    char UUID[BUF_SIZE];
} Instance;

void Instance_Init(Instance* instance, char* UUID) {
    strcpy(instance->UUID, UUID);
}

void Instance_Process(Instance* instance, int A, int B, char* Type) {
    char instrc_n_path[BUF_SIZE], instrc_r_path[BUF_SIZE], instrc_s_path[BUF_SIZE];
    snprintf(instrc_n_path, BUF_SIZE, "Comp%s/Instrc_n.txt", instance->UUID);
    snprintf(instrc_r_path, BUF_SIZE, "Comp%s/Instrc_r.txt", instance->UUID);
    snprintf(instrc_s_path, BUF_SIZE, "Comp%s/Instrc_s.txt", instance->UUID);

    FILE* instrc_n_file = fopen(instrc_n_path, "w");
    fprintf(instrc_n_file, "n");
    fclose(instrc_n_file);

    FILE* instrc_r_file = fopen(instrc_r_path, "w");
    FILE* instrc_s_file = fopen(instrc_s_path, "w");
    fprintf(instrc_s_file, "P");
    fclose(instrc_s_file);

    instrc_s_file = fopen(instrc_s_path, "r");
    fprintf(instrc_r_file, "%d %d %s", A, B, Type);
    fclose(instrc_r_file);

    char buf[BUF_SIZE];
    do {
        fseek(instrc_s_file, 0, SEEK_SET);
        fread(buf, sizeof(char), BUF_SIZE, instrc_s_file);
        usleep(10000);
    } while (buf[0] == 'P');

    instrc_n_file = fopen(instrc_n_path, "w");
    fclose(instrc_n_file);
}

char* Instance_Read(Instance* instance) {
    usleep(100000);
    char instrc_s_path[BUF_SIZE];
    snprintf(instrc_s_path, BUF_SIZE, "Comp%s/Instrc_s.txt", instance->UUID);
    FILE* instrc_s_file = fopen(instrc_s_path, "r");
    char* result = NULL;
    while (1) {
        char buf[BUF_SIZE];
        fgets(buf, BUF_SIZE, instrc_s_file);
        if (buf[0] == '\0') {
            continue;
        } else {
            if (buf[0] == 'F') {
                fclose(instrc_s_file);
                return "False";
            } else if (buf[0] == 'T') {
                fclose(instrc_s_file);
                return "True";
            } else {
                result = strdup(buf);
                break;
            }
        }
    }
    fclose(instrc_s_file);
    return result;
}

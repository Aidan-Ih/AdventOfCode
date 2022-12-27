#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

    FILE *file = fopen("input1.txt", "r");
    int f = 0;
    int c = fgetc(file);

    int curr_p = 1;
    int first_basement = -1;

    while (c != EOF) {
        if (c == '(') {
            f++;
        }
        else if (c == ')') {
            f--;
        }
        if(f == -1 && first_basement == -1) {
            first_basement = curr_p;
        }
        c = fgetc(file);
        curr_p++;
    }

    printf("Final floor: %d\n", f);
    printf("First basement: %d\n", first_basement);
}
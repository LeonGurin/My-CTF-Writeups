#include <stdio.h>

int main(){
    char v1[17] = "KFWI~6}bGuxqnbU6y";
    printf("%s\n", (const char *)v1);
    for (int i = 0; i <= 99 && *(v1 + i); ++i ){
        *(v1 + i) -= 3;
    }
    printf("%s}\n", (const char *)v1);
}

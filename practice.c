#include <stdio.h>

int main(){
    int a = 7;
    int* ptr = &a;

    printf("%d \n",*ptr);
    printf("%p \n",ptr);


    return 0;
}
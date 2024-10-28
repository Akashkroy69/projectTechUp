#include <stdio.h>


int main(){
    int a = 10;
    printf("value of a : %d",a);
    // this doesn't print the address correctly in 64-bit system as integer crosses the integer size
    printf("Address of a of a : %d",&a);
    // correct format in hexadecimal notation
    printf("Address of a of a : %p",&a);


    int *ptr = &a;
    printf("\n\nAddress of a : %p\n\n",ptr);
    printf("\n\nvalue of a : %d\n",*ptr);
    printf("\n\nvalue of a : %d\n",*(&a));


    int **ptr_of_ptr = &ptr;
    printf("\n\nAddress of ptr : %p\n\n",&ptr);
    printf("\n\nAddress of ptr : %p\n\n",ptr_of_ptr);
    printf("\n\nvalue of ptr : %p\n",*ptr_of_ptr);
}
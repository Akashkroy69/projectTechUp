// Understanding Pointers in C

// Pointers are a powerful feature in C that allow you to directly access and manipulate memory.
//  They store the address of a variable rather than the actual value.
// 1. What is a Pointer?

// A pointer is a variable that holds the memory address of another variable.

#include <stdio.h>

int main(){
    // Here, poninter is a pointer to an integer (int). The * signifies that it is a pointer.
    int *poninter;

    int num = 10;
    poninter = &num; //will store the memory address of num.

    printf(" \nvalue of num : %d \n",num);
    printf(" \nvalue of num(using pointer) : %d \n",*poninter); //Dereferencing a Pointer (*)
// Dereferencing is the process of accessing the value stored at the memory address a pointer holds. 
// The * operator is used to dereference.
    printf(" \naddress of num : %d \n",poninter);

// Null Pointers
// A null pointer is one that doesn’t point to any valid memory location.
int *nullPointer = NULL;
printf(" \naddress of nullpointer : %d \n",nullPointer);




}
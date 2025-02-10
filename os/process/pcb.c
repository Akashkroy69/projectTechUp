#include <stdio.h>
#include <stdlib.h>

int global_var = 10;          // Initialized data segment
int uninit_var;               // BSS segment

int main() {
    int local_var = 20;       // Stack
    int *heap_var = (int *)malloc(sizeof(int));  // Heap
    *heap_var = 30;

    printf("Text Segment: %p\n", (void *)main);
    printf("Initialized Data: %p\n", (void *)&global_var);
    printf("Uninitialized Data (BSS): %p\n", (void *)&uninit_var);
    printf("Heap: %p\n", (void *)heap_var);
    printf("Stack: %p\n", (void *)&local_var);

    free(heap_var);
    return 0;
}
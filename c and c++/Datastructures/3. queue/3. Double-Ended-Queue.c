#include <stdio.h>

#define SIZE 5  

int DoubleEndedQueue[SIZE];
int front = -1;
int rear = -1;
// isFull
int isFull(){
    if (front == 0 && rear == SIZE-1)
    {
        return 1;
    }else{
        return 0;
    }
    
}
// isEmpty()
int isEmpty(){
    if (rear == -1 ||front>rear)
    {
        return 1;
    }else{
        return 0;
    }
    
}

// insert data
void enqueueFront(int element){
    if(isFull()){
        printf("\nthe queue is full. element can't be pushed\n");
    }else{
        if (front == -1 && rear == -1)
        {
            front = 0;
        }
        if(front > 0 && front<=rear){

        }
        DoubleEndedQueue[++rear] = element;
        printf("%d has been added in the QUEUE.",element);

        
    }
}
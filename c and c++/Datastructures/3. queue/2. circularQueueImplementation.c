#include <stdio.h>

#define MAX 5
// circular queue
int circularQueue[MAX];
int front = -1;
int rear = -1;

// enqueue
void enqueue(int element){
    // if full we can't enter
    if((rear+1)%MAX == front){
        printf("\nthe queue is full, overflowed\n %d has not been added in the queue",element);
    }else{
        if(front == -1 && rear == -1){
            front = 0;
        }
        rear = (rear + 1) % MAX;
        circularQueue[rear] = element;
        printf("\n%d has been added in the circular QUEUE.\n",element);

    }
}
// dequeue
int dequeue(){
    if(front == -1 && rear == -1){
        printf("\nthe queue is empty, underflowed\n");
        return -1;
    }else if (front>rear)
    {
        front = rear = -1;
        return -1;
    }else{
        int element = circularQueue[front];
        circularQueue[front] = -1;
        front = (front + 1)% MAX;
        printf("\n%d has been deleted in the circular QUEUE.\n",element);
        return element;
    }
}


int main(){
    enqueue(12);
    enqueue(22);
    enqueue(42);
    enqueue(64);
    enqueue(62);
    enqueue(623);
    dequeue();
    dequeue();
    enqueue(200);



}
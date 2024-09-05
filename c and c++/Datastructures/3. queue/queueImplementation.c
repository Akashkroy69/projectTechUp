#include <stdio.h>

#define SIZE 5  

int queue[SIZE];
int front = -1;
int rear = -1;

// isFull
int isFull(){
    if (rear == SIZE-1)
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
void enqueue(int element){
    if(isFull()){
        printf("the queue is full");
    }else{
        if (rear == -1)
        {
            front = 0;
        }
        queue[++rear] = element;
        printf("%d has been added in the QUEUE.",element);

        
    }
}
// delete from queue
int dequeue(){
    if (isEmpty())
    {
        printf("The queue is empty");
        return -1;
    }else{
        int element = queue[front];
        queue[front++] = -1;
        if (front>rear)
        {
            // starting point
           front = rear = -1;
        }
        printf("%d has been deleted from the queue.",element);
        return element;
    }
    
}

// Function to display the queue elements
void display() {
    int i;
    if (isEmpty()) {
        printf("Queue is empty!\n");
    } else {
        printf("Queue elements are: ");
        for (i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}
// Main function to test the queue implementation
int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    enqueue(50);

    display();

    dequeue();
    dequeue();

    display();

    enqueue(60);
    display();

    return 0;
}

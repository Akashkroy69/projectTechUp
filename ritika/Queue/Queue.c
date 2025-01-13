#include <stdio.h>

#define MAX 5
int QUEUE[MAX];
int front = -1;
int rear = -1;
// 1. enqueue (insertion)
// 2. dequeue (deletion)
// 3. peek--> viewing the front element
// 4. display()
// 5. isFull()
// 6. isEmpty()
int isEmpty(){
    if(front == -1 && rear == -1){
        printf("\nQueue is empty\n");
        return 1; // 1 signals that answer is yes
    }else{
        printf("\nQueue is not empty\n");
        return 0; //0 signals that answer is no
    }

}
int isFull(){
    if(rear == MAX -1){
        printf("\nQueue is full\n");
        return 1;
    }else{
        printf("\nQueue is not full\n");
        return 0;

    }
    
}
// 
void enqueue(int element){

}

int main(){
    int answer = isEmpty();
    printf("%d",answer);
    isFull();


   enqueue(10);

}



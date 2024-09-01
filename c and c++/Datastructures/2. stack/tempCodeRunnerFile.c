#include <stdio.h>
// stack implementation
// operations: 
// 1. push
// 2. pop
// 3. display
// 4. isEmpty
// 5. isFull
// 6. peek: to pick the top element from the stack
// TERMS:
// 1. underflow <--- when stack is empty
// 2. overflow <-- when stack is full
#define MAX 10
int stack[MAX];
int top = -1;

// 1. push
void push(int element){
  
    if(top == MAX-1){
        printf("stack Overflow error, stack is full");
        return;
    }else{
        stack[++top] = element;
        printf("%d has been added to the top of the stack",element);
    }
}
// 2. pop
int pop(){
    if(top == -1){
        printf("stack underflow. stack is empty");
        return -1;
    }else{
        int popped = stack[top];
        stack[top--] = -1;
        printf("%d is popped",popped);
        return popped;
    }
}
int peek(){
    if(top == -1){
        printf("is empty");
        return -1;
    }else{
        return stack[top];
    }
}
void display(){
    if(top == -1){
        printf("is empty");
        
    }else{
        printf("stack elements:");
        for(int i =0; i<=top;i++){
            printf("%d ",stack[i]);
        }
    }
}
// is empty?
int isEmpty(){
    return top == -1;
}
// is full?

int isFull(){
    return top == MAX -1;
}

int main(){
    printf("Stack implementation");
    push(10);
    push(20);
    push(30);
    push(40);

}
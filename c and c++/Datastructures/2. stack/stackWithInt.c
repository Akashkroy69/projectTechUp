#include <stdio.h>

#define MAX 10
int stack[MAX];
int top = -1;

// 1. push
void push(int element){
  
    if(top == MAX-1){
        printf("\nstack Overflow error, stack is full\n");
        return;
    }else{
        stack[++top] = element;
        printf("\n%c has been added to the top of the stack\n",element);
    }
}
// 2. pop
int pop(){
    if(top == -1){
        printf("\nstack underflow. stack is empty\n");
        return -1;
    }else{
        int popped = stack[top];
        stack[top--] = -1;
        printf("\n%c is popped\n",popped);
        return popped;
    }
}
int peek(){
    if(top == -1){
        printf("\nis empty\n");
        return -1;
    }else{
        return stack[top];
    }
}
void display(){
    if(top == -1){
        printf("\nis empty\n");
        
    }else{
        printf("\nstack elements:\n");
        for(int i =0; i<=top;i++){
            printf("%c ",stack[i]);
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
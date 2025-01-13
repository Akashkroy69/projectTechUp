#include <stdio.h>
// stack implementation
// operations: 
// 1. push
// 2. pop
// 3. display
// 4. isEmpty
// 5. isFull
// 6. peek: to see the top element from the stack(here we don't pop the element from the stack, we just see the element on the top)
// TERMS:
// 1. underflow <--- when stack is empty
// 2. overflow <-- when stack is full
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
        stack[top] = -1;
        top = top -1;
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

// int main(){
//     printf("\nStack implementation\n");
//     push(10);
//     push(20);
//     push(30);
//     push(40);

 }
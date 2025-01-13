#include <stdio.h>
// push
// pop
// peek
// isEmpty
// isFull
// display
// terms: stack overflow, stack underflow

// constant define
#define MAX 5
int stack[MAX];
int top = -1;

// push
void push(int element){
//   if stack is full then we can't push more elements. display stack overflow
//   else
// 4
  if(top >=MAX-1){
    printf("\nstack overflow, we can't push more elements (%d) onto the stack\n",element);   
  }else{
      stack[++top] = element;
      printf("\nelement %d has been pushed onto the stack\n",element);
  }

}
int pop(){
  //if top = -1,we will print "stack underflow,we cant pop any element"
  if(top==-1)
  {
    printf("\nstack underflow,we cant pop any element as already empty\n");
    return -1; 
  }else{
    int x = stack[top];
    stack[top] = -1;
    top--;
    printf("\n %d has been popped\n",x);
    return x;
  }
}
int main(void) {
  push(10);
  push(20);
  push(30);
  push(40);
  push(50);
  push(60);
  pop();
  pop();
  pop();
  pop();
  pop();
  pop();
  pop();
  return 0;
}
// time complexity of push and pop is O(1)
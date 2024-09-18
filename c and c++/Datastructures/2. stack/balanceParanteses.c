#include <stdio.h>
#include "stack.c"
// function to check balance paranthese
void isParathesisBalanced(char arr[],int size){

    int i =0; 
    while (i < size)
    {
        if (arr[i]=='(')
        {
           push('(');
        }else if (arr[i] == ')')
        {
           char ch =  pop();
        }
        i++;
    }

    if (isEmpty()==1)
    {
        printf("\nbalanced\n");
    }else{
        printf("\nnot balanced\n");

    }
    
    

}

int main(){

    char exp[] = "((A+B)+(C+D))";
    int size = sizeof(exp)/sizeof(char);
    printf("size of exp: %d",size);
    isParathesisBalanced(exp,size);

}
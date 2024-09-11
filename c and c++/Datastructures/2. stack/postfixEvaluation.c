#include <stdio.h>
#include "stack.c"

int postfixEvaluation(char *postfixExp){
    int i =0;

    while (postfixExp[i]=='\0')
    {
        char ch = postfixExp[i++];
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9'))
        {
           push(ch);
        }else{
            int firstPopThatWorksAsSecondOperand = pop()-'0';
            int secondPopThatWorksAsFirstOperand = pop() - '0';
            int result =  secondPopThatWorksAsFirstOperand + firstPopThatWorksAsSecondOperand;
            push(result);


        }
        
    }
    
    return pop();
}

int main(){
    // 2+3*4 -----> 2,3,4*+
    char postfix[] = '2+3*4';
    int value = postfixEvaluation(postfix);
    printf("the value of the postfix evaluation: %d",value);

    return 0;

}
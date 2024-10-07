#include <stdio.h>
#include "stackWithInt.c"


int postfixEvaluation(char *postfixExp){
    int i =0;

    while (postfixExp[i]!='\0')
    {
        char ch = postfixExp[i++];
        if ((ch >= '0' && ch <= '9'))
        {
           push(ch - '0');
        }else{
            int firstPopThatWorksAsSecondOperand = pop();
            int secondPopThatWorksAsFirstOperand = pop();
            int result;
            switch (ch)
            {
            case '+':
                 result =  secondPopThatWorksAsFirstOperand + firstPopThatWorksAsSecondOperand;
                 push(result);
                break;
             case '-':
                 result =  secondPopThatWorksAsFirstOperand - firstPopThatWorksAsSecondOperand;
                 push(result);
                break;
             case '*':
                  result =  secondPopThatWorksAsFirstOperand * firstPopThatWorksAsSecondOperand;
                 push(result);
                break;
             case '/':
                 result =  secondPopThatWorksAsFirstOperand / firstPopThatWorksAsSecondOperand;
                 push(result);
                break;
            default:
                break;
            }
           


        }
        
    }
    
    return pop();
}

int main(){
//     // 2+3*4 -----> 2,3,4*+
    char postfix[] = "324+*2+";
    int value = postfixEvaluation(postfix);
    printf("the value of the postfix evaluation: %d",value);

//     return 0;

}
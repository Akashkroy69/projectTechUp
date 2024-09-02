#include <stdio.h>
#include "stack.c"

int precedenceValue(char ch){
    if (ch == '+' || ch == '-')
    {
        return 1;
    }else if (ch == '*' || ch == '/')
    {
        return 2;
    }else if (ch == '^')
    {
        return 3;
    }

    return 0;
    
}


void infixToPostfix(char infix[], char postfix[])
{
    int i=0, j = 0;
    char ch;
        // printf("test %d",i);

    while (infix[i] != '\0')
    {
         ch = infix[i++];
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
        {
            postfix[j++] = ch;
        }
        else if (ch == '(')
        {
            push(ch);
        }
        else if (ch == ')')
        {
            while (!isEmpty() && peek() != '(')
            {
                postfix[j++] = pop();
            }
            pop();  //popping ) from stack
        }else{
            if (precedenceValue(ch)>0)
            {
                while (!isEmpty() && precedenceValue(ch)<= precedenceValue(peek()))
                {
                    postfix[j++] = pop();
                }
                push(ch);
            }
            
        }
    }

    while (!isEmpty())
    {
        postfix[j++] = pop();
    }
    postfix[j] = '\0';
    
}


int main()
{
    char infixExpression[] = "(A+B)-C+D*C";
    char postfixOutExpression[100];

    int size = sizeof(infixExpression) / sizeof(infixExpression[0]);

infixToPostfix(infixExpression,postfixOutExpression);

printf("\ninfix: %s\n",infixExpression);
printf("\npostfix: %s\n",postfixOutExpression);

    // for (int i = 0; i < size; i++)
    // {
    //     if (infixExpression[i] == '+' || infixExpression[i] == '-' || infixExpression[i] == '*' || infixExpression[i] == '/' || infixExpression[i] == '^' || infixExpression[i] == '(' || infixExpression[i] == ')')
    //     {
    //         push(infixExpression[i]);
    //     }
    //     else
    //     {
    //     }
    // }
}
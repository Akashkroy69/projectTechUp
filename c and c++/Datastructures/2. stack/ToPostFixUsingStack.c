#include <stdio.h>
#include "stack.c"

int precedenceValue(char ch)
{
    if (ch == '+' || ch == '-')
    {
        return 1;
    }
    else if (ch == '*' || ch == '/')
    {
        return 2;
    }
    else if (ch == '^')
    {
        return 3;
    }

    return 0;
}

void infixToPostfix(char *infix, char *postfix)
{
    int i = 0, j = 0;
    char ch;
    // printf("test %d",i);
    char tempChar;
    while (infix[i] != '\0')
    {
        tempChar = infix[i-1];
        ch = infix[i++];
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9'))
        {
            postfix[j++] = ch;
            if ((tempChar >= 'a' && tempChar <= 'z') || (tempChar >= 'A' && tempChar <= 'Z') || (tempChar >= '0' && tempChar <= '9'))
            {
                postfix[j++] = ',';
            }
            
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
            pop(); // popping ) from stack
        }
        else
        {
            if (precedenceValue(ch) > 0)
            {
                while (!isEmpty() && precedenceValue(ch) <= precedenceValue(peek()))
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

// int main()
// {
//     // char infixExpression[] = "(A+B)-C+D*C";
//     char infixExpression[] = "5*2+(16/2^3-3*2)+14/7";

//     char postfixOutExpression[100] = "";

//     int size = sizeof(infixExpression) / sizeof(infixExpression[0]);

//     infixToPostfix(infixExpression, postfixOutExpression);

// printf("\n========Result===============\n");
//     printf("\ninfix: %s\n", infixExpression);
//     printf("\npostfix: %s\n", postfixOutExpression);
// printf("\n==============================\n");


//     // for (int i = 0; i < size; i++)
//     // {
//     //     if (infixExpression[i] == '+' || infixExpression[i] == '-' || infixExpression[i] == '*' || infixExpression[i] == '/' || infixExpression[i] == '^' || infixExpression[i] == '(' || infixExpression[i] == ')')
//     //     {
//     //         push(infixExpression[i]);
//     //     }
//     //     else
//     //     {
//     //     }
//     // }
// }
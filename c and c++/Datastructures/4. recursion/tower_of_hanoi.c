#include <stdio.h>


void move(int n, char x, char y){
    printf("\n%d number plate is moved from %c --> %c\n",n,x,y);
}

void TOH(int n, char A, char B, char C){
    if (n==1)
    {
        move(n,A,B);
        return;
    }

    TOH(n-1,A,C,B);
    move(n,A,B);
    TOH(n-1,C,B,A);
}

int main(){
    int n = 4;
    char source = 'A';
    char destination = 'B';
    char auxiliary = 'C';
    TOH(n,source,destination,auxiliary);
}
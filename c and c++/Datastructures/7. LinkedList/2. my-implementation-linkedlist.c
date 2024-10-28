#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Head
{
    struct Node* firstNode;
};


struct Node* createNode(int value){

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
   newNode->data = value;
   newNode->next = NULL;
   printf("\nnode is created with element %d\n",newNode->data);
   return newNode;

}


int main(){
    struct Head* head = (struct Head*)malloc(sizeof(struct Head));

    struct Node* node1 = createNode(10);
    head->firstNode = node1;

    
    struct Node* node2 = createNode(20);
    node1->next = node2;

    struct Node* node3 = createNode(30);
    node2->next = node3;

    printf("\nhead address:%d, first node: %p \n",(void*)head,(void*)head->firstNode);
    printf("\nnode1 data--> %d, address:%p, address of next: %p\n",node1->data,(void*)node1,(void*)node1->next);
    printf("\nnode2 data--> %d, address: %p, address of next: %p\n",node2->data,(void*)node2,(void*)node2->next);
    printf("\nnode3 data--> %d, address: %p, address of next: %p\n",node3->data,(void*)node3,(void*)node3->next);

}

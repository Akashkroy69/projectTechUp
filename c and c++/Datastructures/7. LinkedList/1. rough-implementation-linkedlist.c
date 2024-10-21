#include <stdio.h>

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
   printf("\nnode is created\n");
   return newNode;

}


int main(){
    struct Head* head = (struct Head*)malloc(sizeof(struct Head));

    struct Node* node1 = createNode(10);
    head->firstNode = node1;

    
    struct Node* node2 = createNode(20);
    struct Node* node3 = createNode(30);

    
    node1->next = node2;
    node2->next = node3;
    node3->next = NULL;


    printf("\nnode1 data--> %d, address:%d\n",node1->data,&node1);
    printf("\nnode2 data--> %d, address: %d\n",node2->data,&node2);
    printf("\nnode3 data--> %d, address: %d\n",node3->data,&node3);

    printf("\nHead --> %d\n",head);
    printf("\nnode1 next--> %d\n",node1->next);
    printf("\nnode2  next--> %d\n",node2->next);
    printf("\nnode3  next--> %d\n",node3->next);


}

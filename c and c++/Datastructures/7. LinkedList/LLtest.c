#include <stdio.h>
#include <stdlib.h>
struct Node{
    int data;
    struct Node *next;
};

// operations on linked list
// 1. insertion : at begining, at end, at middle
// at beginning
void insertAtBeg(struct Node  **head, int data){
    // new node holds the address of newly allocated memory for the Node
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));

    if(newNode == NULL){
        printf("\nmemory allocation failed\n");
        return;
    }

    newNode->data = data;
    newNode->next = NULL;

    if (*head == NULL)
    {
        // 
        *head = newNode;
        printf("\nfirst node : mod_d-->  %d, mod_p-->%p, data: %d\n",head,head,(*head)->data);
        return;
    }
    newNode->next = *head;
    *head = newNode;
}

void insertAtEnd(struct Node **head, int data){
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
     if(newNode == NULL){
        printf("\nmemory allocation failed\n");
        return;
    }

    newNode->data = data;
    newNode->next = NULL;

    // for adding in end
    struct Node *temp = *head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;
}

void display(struct Node *head){
    if (head == NULL)
    {
        printf("\nThe linked list is empty.\n-------\n");
        return;
    }
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("\nNode address: %p, data: %d, next node address: %p\n--------\n",temp,temp->data,temp->next);
        temp = temp->next;
    } 
    
}

int main(){
    struct Node* head = NULL;
    display(head);
    printf("\n*****\n");
    insertAtBeg(&head,10); 
    display(head);
    printf("\n*****\n");
    insertAtBeg(&head,20); 
    display(head);
    printf("\n*****\n");
    insertAtBeg(&head,30); 
    display(head);
    printf("\n*****\n");
    insertAtBeg(&head,40); 
    display(head);
    printf("\n*****\n");
    insertAtEnd(&head,50);
    insertAtEnd(&head,60);
    display(head);




}
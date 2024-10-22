#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next; //self referencing poniter
};

void insertAtStart(struct Node** head,int data){

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));   //understand more on this
    if(newNode == NULL){
        printf("\nNode creation failed\n");
        return;
    }
    newNode->data = data;
    newNode->next = *head;
    *head = newNode;
    printf("Inserted %d at the beginning.\n", data);
}

void inserAtEnd(struct Node* head,int data){
    
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));   //understand more on this
    if(newNode == NULL){
        printf("\nNode creation failed\n");
        return;
    }
    newNode->data = data;
    newNode->next = NULL;

    if(head == NULL){
      head = newNode;
      return;
    }

    struct Node* temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;  // Traverse to the last node
    }

    temp->next = newNode;
    printf("Inserted %d at the end.\n", data);
}

void deleteNode(struct Node** head,int data){


}


void printAll(struct Node* head){
    if (head ==NULL)
    {
        printf("\nLinkked list is empty\n");
        return;
    }
    
    struct Node* temp = head;
    int count  = 0;
    while (temp != NULL)
    {
        count++;
        printf("\nelement number %d is %d\n",count,temp->data);
        temp = temp->next;
    }
    

}

int main(){

// insertion of 10 in the LL
    struct Node* head = NULL;

    insertAtStart(&head,10);
    insertAtStart(&head,20);
    insertAtStart(&head,30);

    inserAtEnd(head,50);

    printAll(head);

}
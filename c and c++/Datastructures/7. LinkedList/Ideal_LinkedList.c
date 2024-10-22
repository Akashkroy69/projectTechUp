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
    
    newNode->next = head;
    *head = newNode;
    printf("Inserted %d at the beginning.\n", data);
}

void inserAtEnd(struct Node** head,int data){
    
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));   //understand more on this
    if(newNode == NULL){
        printf("\nNode creation failed\n");
        return;
    }

    if(*head == NULL){
      *head = newNode;
      return;
    }

    struct Node* temp = *head;
    while (temp->next != NULL)
    {
        temp = temp->next;  // Traverse to the last node
    }

    temp->next = newNode;
    printf("Inserted %d at the end.\n", data);
}

int main(){

// insertion of 10 in the LL
    struct Node* head = NULL;

    insertAtStart(&head,10);
}
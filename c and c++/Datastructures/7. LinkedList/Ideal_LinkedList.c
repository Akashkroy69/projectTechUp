#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next; //self referencing poniter
};

// insertion at beginning
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

// insertions at end
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

// deletion by number
void deleteNode(struct Node** head,int data){

    if(*head == NULL){
        printf("\nLinked list is empty\n");
        return;
        
    }
    
        struct Node* temp = *head;
        if (temp->data == data)
        {
            *head = temp->next;
            free(temp);
            printf("Deleted node with value %d.\n", data);
            return;
        }else{
            struct Node* prev;
            while (temp->data != data)
            {
                prev = temp;
                temp = temp->next;
                if(temp == NULL){
                    printf("%d is not found in the linked list.",data);    
                    return;
                }
            }
            prev->next = temp->next;
            free(temp);
            printf("Deleted node with value %d.\n", data);
            return;
        }
}


// displaying elements
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

void freeResources(struct Node** head){
    struct Node *temp = *head;
    if (temp == NULL)
    {
        printf("\nthe linked list is empty\n");
    }else{
        while (temp != NULL)
        {
            struct Node *currentNode = temp;
            temp = temp->next;
            free(currentNode);
        }

        printf("\nxxxxxxxx----All clear----xxxxxxxx\n");
        *head = NULL;
        return;
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

    deleteNode(&head,50);
    printf("\n========\n");
    printAll(head);

    freeResources(&head);
    printAll(head);


}
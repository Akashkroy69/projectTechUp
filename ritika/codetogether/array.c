// write a program to insert at beg, end, at given pos.
#include<stdio.h>

// insert at the beg
int insertAtBeg(int arr[],int size,int data)
{
  // shifting
  for(int i = size; i>=1;i--){
    arr[i] = arr[i-1];
  }
  // insertion at beg
    arr[0] = data;
    // size incr as one element has been inserted
    return size+1;
}
// insert at end
int insertatend(int arr[],int size, int data)
{
     arr[size] = data;
    
   return size+1; 
}
// insert at given pos
int insertatpos(int arr[],int size,int data,int pos)
{
   // shifting
  for(int i = size; i>pos;i--){
    arr[i] = arr[i-1];
  }
  
    arr[pos] = data;
    
    return size+1;
   
}

int main(){
    //array of size 100 
    int arr[100];
    
    int size=0;

    size = insertatend(arr,size,10);
    size = insertAtBeg(arr,size,40);
    size=insertatpos(arr,size,50,1);
    
}

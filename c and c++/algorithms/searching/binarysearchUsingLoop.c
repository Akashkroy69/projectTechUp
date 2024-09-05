#include <stdio.h>

int binarySearchUsingLoop(int *arr,int size, int element){
    int firstIndex = 0,lastIndex = size-1;

    while (firstIndex<=lastIndex)
    {
        int middleIndex = (firstIndex+lastIndex)/2;
      if (arr[middleIndex] == element)
      {
        return middleIndex;
      }else if (arr[middleIndex]>element)
      {
        lastIndex = lastIndex -1;
        
      }else{
        firstIndex = middleIndex +1;
      }
       
    }
    return -1; 
    
}

int main()
{
    //  int array[] = {23,1,2,44,21,56};
     int array[] = {1,2,3,4,5,6,21};

        int size = sizeof(array)/sizeof(int);
        int element = 1;
    int indexOfElement = binarySearchUsingLoop(array,size,element);
     
     if (indexOfElement>=0)
     {
        printf("element %d is found at %d",element,indexOfElement);
     }else{
        printf("element %d is not found",element);

     }
}
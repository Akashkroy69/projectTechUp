#include <stdio.h>

int binarysearch(int arr[], int startIndex, int lastIndex, int element)
{
    if (startIndex > lastIndex)
    {
      return -1;
    }
    

    int midleIndex = (startIndex + lastIndex) / 2;
    if (arr[midleIndex] == element)
    {
        return midleIndex;
    }
    else if (arr[midleIndex] > element)
    {
        lastIndex = midleIndex-1;
        startIndex = startIndex;
        return binarysearch(arr,startIndex,lastIndex,element);
    }else
    
    {
        startIndex = midleIndex+1;
        lastIndex = lastIndex;
       return binarysearch(arr,startIndex,lastIndex,element);

    }
}

int main()
{
    //  int array[] = {23,1,2,44,21,56};
     int array[] = {1,2,3,4,5,6,21};

        int size = sizeof(array)/sizeof(int);
        int element = 1;
    int indexOfElement = binarysearch(array,0,size-1,element);
     
     if (indexOfElement>=0)
     {
        printf("element %d is found at %d",element,indexOfElement);
     }else{
        printf("element %d is not found",element);

     }
}
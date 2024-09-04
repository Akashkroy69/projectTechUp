#include <stdio.h>

int linearSearch(int arr[],int size, int element){


    for (int i = 0; i < size; i++)
    {

        if (arr[i]==element)
        {
            return i;
        }
        
    }
    

return -1;
}
int main(){
    int array[] = {23,1,2,44,21,56};
        int size = sizeof(array)/sizeof(int);
        int element = 21;
    int indexOfElement = linearSearch(array,size,element);
     
     if (indexOfElement>=0)
     {
        printf("element %d is found at %d",element,indexOfElement);
     }else{
        printf("element %d is not found",element);

     }
     

}
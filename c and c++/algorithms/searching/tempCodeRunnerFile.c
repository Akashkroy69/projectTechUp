#include <stdio.h>

int linearSearch(int *arr, int element){
    int size = sizeof(arr)/sizeof(int);
    printf("==========",size);
    for (int i = 0; i < size; i++)
    {
    printf("==========",i,arr[i]);

        if (arr[i]==element)
        {
            return i;
        }
        
    }
    

return -1;
}
int main(){
    int array[] = {23,1,2,44,21,56};
    int indexOfElement = linearSearch(array,1);
     
     if (indexOfElement>=0)
     {
        printf("element %d is found at %d",1,indexOfElement);
     }else{
        printf("element %d is not found",1);

     }
     

}
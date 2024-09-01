#include <stdio.h>

void bubbleSort(int arr[],int size){
    for (int i = 0; i < size-1; i++)
    {
        for (int j = 0; j < size-i-1; j++)
        {
            if (arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1]=temp;
            }
            
        }
        
    }
    
}


void display(int arr[], int size){
    for (int i = 0; i < size; i++)
    {
        printf("%d ",arr[i]);
    }
    
}
int main(){
    int arr[] = {23,12,3,11,4,22};
printf("Before sorting: ");
     display(arr,sizeof(arr)/sizeof(arr[0]));
    bubbleSort(arr,sizeof(arr)/sizeof(arr[0]));

    printf("after sorting: ");
     display(arr,sizeof(arr)/sizeof(arr[0]));
    return 0;
}
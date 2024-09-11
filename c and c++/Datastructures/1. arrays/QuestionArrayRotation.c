// given an array of integers and a number of rotations, write an algorithm to rotate a given array by k position
//[1,2,3,4,5,6,7] by 3 position ===> [4,5,6,7,1,2,3]
// complexity?

#include <stdio.h>

void reverse(int arr[],int startingIndex, int lastIndex){
 while (startingIndex < lastIndex)
 {
    int temp = arr[startingIndex];
    arr[startingIndex] = arr[lastIndex];
    arr[lastIndex] = temp;
    startingIndex++;
    lastIndex--;
 }
 
    
}

void rotate(int arr[],int size, int posToRotate){

reverse(arr,0,size-1); //[7,6,5,4,3,2,1]
reverse(arr,0,size-posToRotate-1);//[4,5,6,7,3,2,1]
reverse(arr,size-posToRotate,size-1);

}
// time complexity: O(n),O(n-k),O(k)==>O(n)
// space complexity: O(1)


int main(){

    int array[] = {1,2,3,4,5,6,7};
    int size = sizeof(array)/sizeof(int);
    int k = 3;
    rotate(array,size,k);

    for (int i = 0; i < size; i++)
    {
        printf("%d ",array[i]);
    }
    


}
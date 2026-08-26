#include<bits/stdc++.h>
using namespace std;

int  largest_element(vector<int>arr){
    int largest=0;
    int slargest=-1;
    for(int i=0;i<arr.size();i++){
        if (arr[i] > largest){
            slargest=largest;
            largest=arr[i];
        }
        if(arr[i]>slargest && arr[i]<largest){
            slargest=arr[i];
            
        }
    }
    return slargest;
}
void mv_z_end(vector<int> arr2){
    int j = 0;
    for(int i =j;i<arr2.size();i++){
        if (arr2[i]!=0){
            swap(arr2[i],arr2[j]);
            j++;
        }    
    }
    for(int i=0;i<arr2.size();i++){
        cout<<arr2[i]<<endl;
    }
}



int main(){
    vector<int> arr={2,5,4,1,6,1};
    vector<int>arr2={1,0,2,3,2,0,0,4,5,1};
    // cout<<largest_element(arr);
    mv_z_end(arr2);
}


//move zeroes to the end


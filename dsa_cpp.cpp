#include<bits/stdc++.h>
using namespace std;

int largest_element(vector<int>arr){
    int largest=0;
    int slargest=-1;
    for(int i=0;i<arr.size();i++){
        if (arr[i] > largest){
            largest=arr[i];
        }
        if(arr[i]>largest && slargest<largest){
            largest=arr[i];
            slargest=largest;
        }
    }
    return slargest;
}
int main(){
    vector<int> arr={2,5,4,1,6,1};
    cout<<largest_element(arr);
}
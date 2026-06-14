// LARGEST NUMBER IN AN ARRAY

#include<bits/stdc++.h>
using namespace std;
// int main(){
//     vector<int> ar={1,2,6,3,7,4,2};
//     int largest = 0;
//     for(int i=0;i<ar.size();i++){
//         if (ar[i]>largest){
//             largest =ar[i];
//         }
//     }
//     cout<<largest<<endl;
// }

// SECOND LARGEST IN AN ARRAY

// int main(){
//     vector<int> ar={1,2,6,3,7,4,2};
//     int largest = 0;
//     int slargest = INT_MIN;
//     for(int i =0;i<ar.size();i++){
//         if(ar[i]>largest){
//             slargest=largest;
//             largest=ar[i];
            
//         }
//         else if (ar[i]<largest && slargest < ar[i]){
//             slargest=ar[i];
//         }
//     }
//     cout<<slargest<<endl;
// }


// 2 SUM (RETURN NUMBERS)

int main(){
    vector<int> ar={1,2,6,3,7,4,2};
    sort(ar.begin(),ar.end());
    int target= 5;
    int k=0;
    int j = ar.size()-1;
    while(k<j){
        if (ar[k]+ar[j]==target){
            cout<<ar[k]<<","<< ar[j]<<endl;
            break;
        }
        else if(ar[k]+ar[j]>target){
            j--;
        }
        else{
            k++;
        }
    }
}
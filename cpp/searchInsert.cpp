#include <iostream>
using namespace std;

class Solution {
public:
    int searchInsert(int A[], int n, int target) {
        int left=0,right=n-1,middle;
        if(target>A[n-1]) return n;
        if(target<A[0]) return 0;
        while(left<=right)
        {
            middle = (left + right)>>1;
            if(A[middle] == target) return middle;
            else if(A[middle]<target) left = middle+1;
            else right = middle-1;
        }
        if(target>A[left]) return left+1;
        else return left;
    }
};

int main()
{
    Solution S;
    int A[1000],n,target;
    while(cin>>n>>target)
    {
        for(int i=0;i<n;i++) cin>>A[i];
        cout<<S.searchInsert(A,n,target)<<endl;
    }
    return 0;
}

#include <iostream>
using namespace std;

class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        int i=0;
        while(i<n)
        {
            if(A[i]<=0 || A[i]>n || A[i] == i+1)  i++;
            else
            {
                int target=A[i]-1;
                if(A[i]!=A[target])  swap(A[i],A[target]);
                else i++;
            }
        }
        i=0;
        while(A[i]==i+1) i++;
        return i+1;
    }
};

int main()
{
    int A[100],n;
    Solution S;
    while(cin>>n)
    {
        for(int i=0;i<n;i++)    cin>>A[i];
        cout<<S.firstMissingPositive(A,n)<<endl;
    }
    return 0;
}

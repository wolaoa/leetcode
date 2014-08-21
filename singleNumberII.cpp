#include <iostream>
using namespace std;

class Solution {
public:
    int singleNumber(int A[],int n) {
        int one=0,i,j;
        int count[32]={0};
        for(i=0;i<32;i++)
        {
            for(j=0;j<n;j++)
            {
                count[i] += (A[j]>>i)&1;
            }
            if(count[i]%3 == 1)
                one |= (1<<i);
        }
        return one;
    }
};

int main()
{
    Solution S;
    int A[1000];
    int n;
    while(cin>>n)
    {
        for(int i=0;i<n;i++) cin>>A[i];
        cout<<S.singleNumber(A,n)<<endl;
    }
    return 0;
}

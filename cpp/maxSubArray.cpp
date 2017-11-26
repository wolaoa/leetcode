#include <iostream>
#include <vector>
using namespace std;


int maxSubArray(int A[],int n)
{
    int sum,ans,i;
    sum=ans=i=0;
    for(;i<n;i++)
    {
       sum+=A[i];
       if(sum<0)
           sum=0;
       if(sum>ans) ans=sum;
    }
    return ans;
}

int main()
{
    int n;
    int A[1000];
    while(cin>>n)
    {
       for(int i=0;i<n;i++) cin>>A[i];
       cout<<maxSubArray(A,n)<<endl;
    }
    return 0;
}

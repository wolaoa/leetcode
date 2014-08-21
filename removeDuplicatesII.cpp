#include <iostream>
using namespace std;

int removeDuplicates(int A[], int n)
{
    if(n<=1) return n;
    int i=1,j=0,repeat=0;
    while(i<n)
    {
        if(A[i] !=A[j])
        {
              A[++j] = A[i];
              repeat=0;
        }
        else
        {
            if(repeat==0)
            {
               A[++j] = A[i];
               repeat=1;
            }
        }
        i++;
    }
    for(i=0;i<=j;i++)
       cout<<A[i]<<" ";
    cout<<endl; 
    return j+1; 
}

int main()
{
    int n,A[100];
    while(cin>>n)
    {
       for(int i=0;i<n;i++)  cin>>A[i];
       cout<<removeDuplicates(A,n)<<endl;
    }
    return 0;
}

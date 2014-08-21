#include <iostream>
using namespace std;

void sortColors(int A[],int n)
{
    int i=0,j=n-1,k;
    while(A[i]==0) i++;
    while(A[j]==2) j--;

    k=i;
    while(k<=j)
    {
        if(A[k]==0)
        {
            if(A[i]==0)
                k++;
            else
                swap(A[i],A[k]);
            i++;
        }
        else if(A[k]==2)
        {
            swap(A[j],A[k]);
            --j;
        }
        else
            k++;
    }

}
    int main()
    {
        int n,A[100];
        while(cin>>n)
        {
            for(int i=0;i<n;i++) cin>>A[i];
            sortColors(A,n);
        }
        return 0;
    }

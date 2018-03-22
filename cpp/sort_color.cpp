#include<iostream>

using namespace std;

    void sortColors(int A[], int n) {
        int s0,s1,s2,i;
        s0=s1=s2=0;
        for(i=0;i<n;i++)
        {
            if(A[i]==0) s0++;
            else if(A[i]==1) s1++;
            else s2++;
        }
        for(i=0;i<s0;i++) A[i]=0;
        for(i=s0;i<s0+s1;i++) A[i]=1;
        for(;i<n;i++) A[i]=2;

        for(i=0;i<n;i++)
            cout<<A[i] << " ";
        cout<<endl;
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

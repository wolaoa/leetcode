#include<iostream>
#include <vector>
using namespace std;
    int uniquePaths(int m, int n) {
        m--; n--;
        if(m<0 || n<0) return 0;
        if (m==0 || n==0) return 1;

        int i=m+n, j=1, ans=1;
        m=(m<n?m:n);
        n=i-m;
        for(i=m+n,j=1; i>n;i--)
        {
            ans*=i;
            for(;j<=m && ans%j==0; j++)
                ans/=j;
        }
        return ans;
    }

    int main()
    {
        int m,n;
        while(cin>>m>>n)
        {
            cout<<uniquePaths(m,n)<<endl;
        }
        return 0;
    }

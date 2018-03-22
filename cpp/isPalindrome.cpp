#include <iostream>
#include <cmath>
using namespace std;

    bool isPalindrome(int x) {
        int temp=x,n=0,len=0,i;
        if(x<0) return false;

        while(temp>0)
        {
            temp/=10; len++;
        }

        for(i=0;i<len/2;i++)
        {
            n = n*10 + x%10;
            x/=10;
        }
        if(len%2) x/=10;
        return (n==x);
    }

    int main()
    {
        int n;
        while(cin>>n)
        {
            if(isPalindrome(n)) cout<<"Yes"<<endl;
            else cout<<"No"<<endl;
        }
        return 0;
    }

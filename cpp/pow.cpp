#include <iostream>
using namespace std;

double pow(double x,int n)
{
    if(0==x || 1.0==x || n==1) return x;

    if(0==n) return 1;

    if(n<=0)
    {
        x= 1.0/x;
        n = -n;
    }

    double ans=1.0;
    double temp = pow(x,n/2);
    if(n%2)
        ans = x*temp*temp;
    else
        ans = temp*temp;
    return ans;
}

int main()
{
    double x;
    int n;
    while(cin>>x>>n)
        cout<<pow(x,n)<<endl;
    return 0;
}

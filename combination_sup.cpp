#include <iostream>
using namespace std;

int com(int n, int r)
{
    if(n-r < r) r= n-r;   // 减少计算量
    int i,j,s=1;
    for(i=0,j=1;i<r;++i)
    {
       s*=(n-i);
       for(;j<=r && s%j==0; ++j) s/=j;  // 尽量避免越界
     }
    return s;
}

int main()
{
    int a,b;
    while(cin>>a>>b)
        cout<<com(a+b,b)<<endl;
    return 0;
}

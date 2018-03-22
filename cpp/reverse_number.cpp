#include <iostream>
using namespace std;
int reverse(int x) {
    int belowz=0,answer=0;
    if(x<0)
    {
        belowz=1;
        x = -x;
    }
    while(x)
    {
        answer = answer*10 + x%10;
        x/=10;
    }
    if(belowz) answer =-answer;
    return answer;
}

int main()
{
    int n;
    while(cin>>n)
       cout<<reverse(n)<<endl;
    return 0;
}

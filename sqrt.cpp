#include <iostream>
#include <ctime>
#include <cmath>
#include <cstdlib>
using namespace std;
int sqrt(int x) {
    if(x<=0) return 0;

    int left=1,right=x,mid,ans;
    while(left<=right)
    {
       mid = left + (right- left)/2;
       if(mid <= x/mid)
       {
         left = mid+1;
         ans = mid;
       }
       else
         right = mid-1;
    }
    return ans;
}

// Newton
int sqrt1(int x)
{
    if(1==x) return x;
    double r = x/2,last;
    do
    {
        last = r;
        r = (r+ x/r)/2;
    }while(r<last);
    return (int)r;
}
int main()
{
    int a,i;
    clock_t start,finish;
    start = clock();
    for(i=1;i<=1000001;i++) sqrt(i);
    finish = clock();
    cout<<"execution time is:"<<finish-start<<"ms"<<endl;

    start = clock();
    for(i=1;i<=1000001;i++) sqrt1(i);
    finish = clock();
    cout<<"execution time is:"<<finish-start<<"ms"<<endl;
    return 0;
}

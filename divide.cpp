#include <iostream>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {

        int mark =0;
        long long count,temp,ans=0;
        long long dd = dividend;
        long long dr = divisor;
        if((dd>0&&dr<0)||(dd<0&&dr>0) mark=1;
        dd = abs(dd);
        dr = abs(dr);
        if(dividend <divisor || divisor==0 || dividend==0) return 0;

        while(divisor<=dividend)
        {
              count=1;
              temp = divisor;
              while((temp<<1)<=dividend)
              {
                  temp<<=1;
                  count<<=1;
              }
              dividend -= temp;
              ans +=count;
        }
        return mark==0? ans:-ans;
    }
};

int main ()
{
    Solution s;
    int  dd,dr;
    while(cin>>dd>>dr)
        cout<<s.divide(dd,dr)<<endl;
    return 0;
}

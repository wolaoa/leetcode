#include<iostream>
#include <vector>
using namespace std;
vector<int> plusOne(vector<int> &digits)
{
    vector<int>::iterator iter = digits.begin();
    digits.insert(iter,1,0);

    vector<int>::reverse_iterator riter = digits.rbegin();

    int c =1;
    for(;riter!=digits.rend();riter++)
    {
         *riter = *riter+c;
         if(*riter>=10)
         {
            *riter%=10;
            c =1;
         }
         else
         {
            c=0;
         }
    }

    iter = digits.begin();
    if(*iter==0) digits.erase(digits.begin());

    return digits;
}


int main()
{
    int n;
    vector<int> digits;
    vector<int>::iterator iter;

    while(cin>>n)
    {
        digits.clear();
        while(n)
        {
            iter = digits.begin();
            digits.insert(iter,1,n%10);
            n/=10;
        }

        digits = plusOne(digits);

        for(iter=digits.begin();iter!=digits.end();++iter)
            cout<<*iter;
        cout<<endl;
    }
    return 0;
}

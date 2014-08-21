#include <iostream>
#include <string>
#include <cstring>
using namespace std;

class Solution {
public:
    string countAndSay(int n)
    {
        string a="1";
        if(n==1) return a;
        for(int i=2;i<=n;i++)
        {
            string b;
            char current = a[0];
            int j=1,count=1;
            for(j=1;j<a.size();j++)
            {
                if(a[j]==current)
                {
                    count++;
                }
                else
                {
                    char c = count +'0';
                    b+=c;
                    b+=current;
                    current = a[j];
                    count=1;
                }
            }
            char c = count+'0';
            b+=c;
            b+=current;
            a= b;
        }
        return a;
    }
};



int main()
{
    Solution s;
    int n;
    while(cin>>n)
    {
        cout<<s.countAndSay(n)<<endl;
    }
    return 0;
}

#include<iostream>
#include <string>
using namespace std;

class Solution {
public:
/*    int numDecodings(string s) {
        if(s.size()==1|| s.size()==0) return 1;

        int ans=1;
        if(s[0]>='3' && s[0]<='9') ans = numDecodings(s.substr(1));
        else if(s[0]=='0') return 0;
        else
        {
            if(s[1]=='0') ans = numDecodings(s.substr(2));
            else if(s[1]>='7' && s[1]<='9') ans = numDecodings(s.substr(1));
            else  ans = numDecodings(s.substr(1))+numDecodings(s.substr(2));
        }
        return ans;
    } */
    int numDecodings(string s) {
        int len = s.size();
        if(!len || s[0]=='0') return 0;
        if(len==1) return 1;

        int n2 = 1; //f(n-2)
        int n1 = 0; //f(n-1)
        if(s[len-1]!='0') n1=1;
        int c=0;
        for(int i=2;i<=len;i++)
        {
            c=0;
            if(s[len-i]!='0') c+=n1;
            if(s[len-i]=='1' || (s[len-i]=='2' && s[len-i+1]<='6')) c+=n2;
            n2 = n1;
            n1 = c;
        }
        return c;
    }

    int numDecodings1(string s) {
        int len = s.size();
        if(!len || s[0]=='0') return 0;
        int n1=0,n2=1,c=0;
        if(s[len-1]!='0') n1=1;
        for(int i=len-2;i>=0;i--)
        {
            c=0;
            if(s[i]!='0') c=n1;
            if(s[i]=='1' || (s[i]=='2' && s[i+1]<='6')) c+=n2;
            n2 = n1;
            n1 = c;
        }
        return c;
    }
};

int main()
{
    string src;
    Solution S;
    while(cin>>src)
    {
        cout<<S.numDecodings(src)<<endl;
        cout<<S.numDecodings1(src)<<endl;
    }
    return 0;
}

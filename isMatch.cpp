#include<iostream>
#include<cstring>
#include <cstdio>
using namespace std;

class Solution {
public:
    bool isMatch(char *s, char *p) {
        int i=0,j=0,first=0;
        char p1[1000];
        for(i=0;i<strlen(p);i++)
        {
            if(p[i]=='*')
            {
                if(first==1) continue;
                else   first=1;
            }
            else first=0;
            p1[j++] = p[i];
        }
        p1[j]='\0';
        cout<<p1<<endl;
        if(strcmp(p1,".*")==0) return true;
        i=j=0;
        while(i<strlen(s) && j<strlen(p1))
        {
            if(p1[j]=='.')
            {
                if(p1[j+1]=='*')
                {
                     p1+=2;
                     while()
                else
                {
                    i++;  j++;
                }
            }
            else
            {
                if((j+1)<strlen(p1)&& p1[j+1]=='*')
                {
                    if(p1[j]==s[i])
                    {
                        while((i+1)<strlen(s) && s[i+1]==s[i]) i++;
                        i++;
                    }
                    j+=2;
                }
                else
                {
                    if(s[i]==p1[j])
                    {
                        i++; j++;
                    }
                    else
                        return false;
                }
            }
        }
        if(i==strlen(s) && j<=strlen(p1)) return true;
        else return false;
    }
};


int main()
{
    char a[1000],b[1000];
    Solution s;
    while(gets(a) && gets(b))
    {
        if(s.isMatch(a,b)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}

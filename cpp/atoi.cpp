#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

class Solution {
public:
    int INT_MAX = 2147483647;
    int INT_MIN = -2147483648;
    int atoi(const char *str){
        const char* Max = "2147483647";
        const char* Min = "2147483648";
        char b[100];
        int number=0;
        int below=0,i=0,j=0;
        while(str[i]==' ')i++;
        if(i==strlen(str)) return 0;

        if(str[i]=='+'||str[i]=='-')
        {
            if(str[i]=='-') below=1;
            i++;
        }

        for(;i<strlen(str);i++)
        {
            if(str[i]>='0' && str[i]<='9')
                b[j++]=str[i];
            else
                break;
        }
        b[j]='\0';
        int lb = strlen(b);

        if(lb>10)
        {
            if(below) return INT_MIN;
            else return INT_MAX;
        }
        else if(lb==10)
        {
            if(below)
            {
                if(strcmp(b,Min)>=0) return INT_MIN;
                else
                {
                    for(j=0;j<lb;j++)
                        number= number*10 + b[j]-'0';
                }
            }
            else
            {
                if(strcmp(b,Max)>=0) return INT_MAX;
                else
                {
                     for(j=0;j<lb;j++)
                        number= number*10 + b[j]-'0';
                }
            }
        }
        else
        {
            for(j=0;j<lb;j++)
                number= number*10 + b[j]-'0';
        }
        return below>0?-number:number;
    }
};

int main()
{
    Solution s;
    char a[1000];
    while(gets(a))
    {
        cout<<s.atoi(a)<<endl;
    }
    return 0;
}

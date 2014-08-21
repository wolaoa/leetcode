#include <iostream>
#include <cstring>
using namespace std;

    int lengthOfLastWord(const char *s) {
        int len = strlen(s),last=0;
        if(0==len) return 0;
        while(len>=0 && s[--len]==' ');
        if(len<0) return 0;
        while(len>=0 && s[len--]!=' ') last++;
        return last;
    }

int main()
{
    const char s[100]="hello world";
    cout<<lengthOfLastWord(s)<<endl;
    const char s1[100]="  hello    l   world   ";
    cout<<lengthOfLastWord(s1)<<endl;

    const char s2[100]="a";
    cout<<lengthOfLastWord(s2)<<endl;

    const char s3[10]="";
    cout<<lengthOfLastWord(s3)<<endl;

    return 0;
}

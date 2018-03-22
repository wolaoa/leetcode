#include<iostream>
#include<cstring>
using namespace std;

class Solution{
public:
    char *strStr(char *haystack, char *needle){
        char *p1,*obj;
        if(!needle) return haystack;
        while(*haystack!='\0'){
            if(*haystack == *needle){
                obj =needle;
                p1 = haystack;
                while(*obj!='\0' && *obj==*p1){
                    obj++;
                    p1++;
                }
                if(*obj=='\0') return haystack;
            }
            haystack++;
        }
        return NULL;
    }
};

int main(){
    char a[100],b[100];
    char *c;
    Solution S;
    while(cin>>a>>b){
        cout<<a<<" "<<b<<endl;
        c = S.strStr(a,b);
        if(c!=NULL) cout<<*c<<endl;
        else cout<<"empty"<<endl;
    }
    return 0;
}

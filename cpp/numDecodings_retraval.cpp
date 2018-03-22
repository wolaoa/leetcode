#include<iostream>
#include <string>
using namespace std;

class Solution{
public:
    int numDecoding(string s){
        if(!s.size()|| s[0]=='0') return 0;
        return Decoding(s, 0);
    }
    int Decoding(string s,int start){
        if(start==s.size()) return 1;
        int a,c;
        a=c=0;
        if(s[start]!='0'){
            a = Decoding(s,start+1);
        }
        if(start+1<s.size() && (s[start]=='1' || (s[start]=='2' && s[start+1]<='6'))){
            c = Decoding(s,start+2);
        }
        return a+c;
    }
};

int main(){
    Solution S;
    string src;
    while(cin>>src){
        cout<<S.numDecoding(src)<<endl;
    }
    return 0;
}

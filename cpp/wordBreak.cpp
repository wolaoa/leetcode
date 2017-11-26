#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;

class Solution{
public:
    bool wordBreak(string s, unordered_set<string> &dict){
        const int len = s.size();
        if(len==0 || dict.size()==0) return false;
        if(len==1) return dict.find(s)!=dict.end();
        vector<bool> canBreak(len+1,false);
        canBreak[0]=true;
        for(int i=1;i<=len;i++){
            for(int j=i-1;j>=0;j--){
                if(canBreak[j] && dict.find(s.substr(j,i-j))!=dict.end()){
                    canBreak[i]=true;
                    break;
                }
            }
        }
        return canBreak[len];
    }
};
int main(){
    string a,b;
    unordered_set<string> dict;
    int n;
    Solution S;
    while(cin>>a>>n){
        dict.clear();
        for(int i=0;i<n;i++){
            cin>>b;
            dict.insert(b);
        }
        if(S.wordBreak(a,dict)==true) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}

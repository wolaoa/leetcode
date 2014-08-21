#include <iostream>
#include <string>
#include <cstring>
using namespace std;

class Solution{
public:
    int minCut(string s){
        const int len = s.size();
        int i,j;
        bool P[len+1][len+1];
        memset(P,0,sizeof(P));
        int dp[len+1];
        for(i=0;i<=len;i++) dp[i]=i;  // worst case
        for(i=0;i<len;i++){
            for(j=i;j>=0;j--){
                if(s[i]==s[j] && (i-j<2 || P[i-1][j+1])){
                    P[i][j]=true;
                    // match to the start, dp[i]=0
                    dp[i]=min(dp[i],j?dp[j-1]+1:0);
                }
            }
        }
        return dp[len-1];
    }
};

int main(){
    string a;
    Solution S;
    while(cin>>a){
        cout<<S.minCut(a)<<endl;
    }
    return 0;
}

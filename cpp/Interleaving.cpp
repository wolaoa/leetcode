#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if(s1.size() + s2.size() != s3.size()) return false;
        bool judge[1000][1000];
        int i,j;
        judge[0][0]=true;

        for(i=1;i<=s1.size();i++) judge[i][0]= judge[i-1][0] && (s1[i-1]==s3[i-1]);
        for(j=1;j<=s2.size();j++) judge[0][j] = judge[0][j-1] && (s2[j-1]==s3[j-1]);

        for(i=1;i<=s1.size();i++)
        {
            for(j=1;j<=s2.size();j++)
            {
               judge[i][j] = (judge[i][j-1] && s2[j-1]==s3[i+j-1]) || (judge[i-1][j]&& s1[i-1]==s3[i+j-1]);
            }
        }
        return judge[s1.size()][s2.size()];
    }
};

int main()
{
    string s1,s2,s3;
    Solution s;
    while(cin>>s1>>s2>>s3)
    {
        if(s.isInterleave(s1,s2,s3)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}

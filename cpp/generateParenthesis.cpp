#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> vi;
    void generateOne(int left,int right,string s)
    {
       if(left==0)
       {
           vi.push_back(s+string(right,')'));
           return ;
       }
       if(left>=right)
           generateOne(left-1,right,s+'(');
       else
       {
           generateOne(left-1,right,s+'(');
           generateOne(left,right-1,s+')');
       }
    }
    vector<string> generateParenthesis(int n) {
        int left=n,right=n;
        vi.clear();
        generateOne(n,n,"");
        return vi;
    }
};

int main()
{
    Solution S;
    int n;
    while(cin>>n)
    {
        vector<string> vi;
        vi=S.generateParenthesis(n);
        for(int i=0;i<vi.size();i++) cout<<vi[i]<<endl;
    }
    return 0;
}

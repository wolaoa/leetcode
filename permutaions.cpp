#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > ans;
    vector<int> print;
    vector<int> mark;
    int length;
    void DFS(int len,vector<int> &num){
        if(len==length)
        {
            ans.push_back(print);
            return;
        }
        for(int i=0;i<length;i++)
        {
           if(mark[i]==0)
           {
              print[len]= num[i];
              mark[i]=1;
              DFS(len+1,num);
              mark[i]=0;
            }
        }
    }
    vector<vector<int> > permute(vector<int> &num) {
        length=num.size();
        ans.clear();
        if(length<=0) return ans;
        print.clear();
        print.resize(length);
        mark.clear();
        mark.resize(length);
        DFS(0,num);
        return ans;
    }
};
int main()
{
    int n;
    vector<int> v;
    vector<vector<int> > ans;
    Solution S;
    while(cin>>n)
    {
        v.clear();
        ans.clear();
        for(int i=0;i<n;i++)
        {
            int num;
            cin>>num;
            v.push_back(num);
        }
       ans = S.permute(v);
       for(int j=0;j<ans.size();j++)
       {
           for(int k=0;k<ans[0].size();k++)
                cout<<ans[j][k]<<" ";
            cout<<endl;
       }
    }
    return 0;
}

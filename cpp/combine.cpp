#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > ans;
    vector<int> vi;
    int k_start,n_start;
    void DFS(int Count,int start)
    {
        if(Count== k_start)
        {
            ans.push_back(vi);
            return;
        }
        for(int i=start;i<n_start;i++)
        {
            vi[Count] = i+1;
            DFS(Count+1, i+1);
        }
    }
    vector<vector<int> > combine(int n, int k) {
        ans.clear();
        vi.resize(k);
        k_start = k;
        n_start = n;
        DFS(0,0);
        return ans;
    }
};

int main()
{
    vector<vector<int> > ans;
    int n,k;
    Solution S;
    while(cin>>n>>k)
    {
        ans = S.combine(n,k);
        if(!ans.empty())
        {
            for(int i=0;i<ans.size();i++)
            {
                for(int j=0;j<ans[0].size();j++)
                    cout<<ans[i][j]<<" ";
                cout<<endl;
            }
        }
    }
    return 0;
}

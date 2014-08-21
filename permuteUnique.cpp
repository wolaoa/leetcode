#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int> > vi;
    vector<int> types;
    vector<int> counts;

    void generatePermute(int len,vector<int> seq)
    {
        if(len==0)
        {
            vi.push_back(seq);
            return;
        }
        for(int i=0;i<types.size();i++)
        {
            if((counts[i])>0)
            {
                counts[i]--;
                seq.push_back(types[i]);
                generatePermute(len-1, seq );
                seq.pop_back();
                generatePermute(len,seq);
                counts[i]++;
            }
        }
    }

    vector< vector<int> > permuteUnique(vector<int> &num) {
//    void permuteUnique(vector<int> &num) {

        vi.clear();
        types.clear();
        counts.clear();
        if(num.size()==0) return vi;

        sort(num.begin(),num.end());
        int j=0;
        types.push_back(num[0]);
        counts.push_back(1);
        for(int i=1;i<num.size();i++)
        {
            if(num[i]==types.back())
            {
                counts.back()++;
            }
            else
            {
                types.push_back(num[i]);
                counts.push_back(1);
            }
        }
        vector<int> temp;
        temp.clear();
        generatePermute(num.size(),temp);
        return vi;
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
       ans = S.permuteUnique(v);
       for(int j=0;j<ans.size();j++)
       {
           for(int k=0;k<ans[0].size();k++)
                cout<<ans[j][k]<<" ";
            cout<<endl;
       }
    }
    return 0;
}

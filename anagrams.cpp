#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {
        int i;
        map<string, vector<string> > vset;
        for(i=0;i<strs.size();i++)
        {
            string key = strs[i];
            sort(key.begin(),key.end());
            vset[key].push_back(strs[i]);
        }
        vector<string> result;
        map<string, vector<string> >::iterator iter;
        for(iter = vset.begin();iter!=vset.end(); iter++)
        {
            if(iter->second.size()>1)
            {
                vector<string>::iterator viter;
                for(viter=iter->second.begin(); viter!=iter->second.end();viter++)
                    result.push_back(*viter);
            }
        }
        return result;
    }
};

int main()
{
    Solution s;
    vector<string> strs,ans;
    int n;
    string con;
    while(cin>>n)
    {
        strs.clear();
        ans.clear();
        getwchar();
        for(int i=0;i<n;i++)
        {
            getline(cin,con);
            strs.push_back(con);
        }

        for(int k=0;k<strs.size();k++) cout<<strs[k]<<endl;
        ans = s.anagrams(strs);
        for(int j=0;j<ans.size();j++) cout<<ans[j]<<" ";
        cout<<endl;
    }
    return 0;
}

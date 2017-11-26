#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

class Solution {
public:
    string getPrefix(string a,string b)
    {
        string ans;
        for(int i=0;i<a.size() && i<b.size();i++)
        {
            if(a[i]==b[i])  ans+=a[i];
            else break;
        }
        return ans;
    }
    string commonPrefix(int left,int right, vector<string> &strs)
    {
        cout<<left<<" "<<right<<endl;
        if(left>=right) return strs[left];
        if(left+1==right) return getPrefix(strs[left],strs[right]);
        int middle = ((right-left)>>1) + left;
        cout<<"middle : "<<middle<<endl;
        return getPrefix(commonPrefix(left,middle,strs),commonPrefix(middle+1,right,strs));
    }
    string longestCommonPrefix(vector<string> &strs) {
        int i=0,len=strs.size();
        string a;
        if(len<=0) return a;
        return commonPrefix(0,len-1,strs);
    }
    string longestCommonPrefixII(vector<string> &strs) {
        string a;
        if(strs.size()<=0) return a;
        a= strs[0];
        for(int i=1;i<strs.size();i++) a= getPrefix(a,strs[i]);
        return a;
    }
};

int main()
{
    Solution S;
    string a;
    vector<string> strs;
    int n;
    while(cin>>n)
    {
        getchar();
        strs.clear();
        for(int i=0;i<n;i++)
        {
            getline(cin,a);
            strs.push_back(a);
        }
        a = S.longestCommonPrefix(strs);
        if(a.size()==0) cout<<"No common prefix exist"<<endl;
        else cout<<a<<endl;

        a= S.longestCommonPrefixII(strs);
        if(a.size()==0) cout<<"No common prefix exist"<<endl;
        else cout<<a<<endl;

    }
    return 0;
}

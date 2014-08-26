#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string ans;
    int num_k,length,count;
    vector<int> mark;
    void DFS(int len,string s){
        if(len==length)
        {
            count++;
            if(count==num_k)
               ans = s;
            return;
        }
        for(int i=0;i<length;i++)
        {
           if(mark[i]==0)
           {
              char tmp = '0'+i+1;
              mark[i]=1;
              s[len]=tmp;
              DFS(len+1,s);
              mark[i]=0;
            }
        }
    }
    int fac(int n)
    {
        int ret=1;
        for(int i=2;i<=n;i++)
            ret*=i;
        return ret;
    }
   string getPermutation( int n, int k) {
        ans.clear();
        if(n==0 || k>fac(n)) return ans;
        num_k = k;
        length = n;
        count=0;
        mark.resize(n);
        ans.resize(n);
        DFS(0,);
        return ans;
    }
};
int main()
{
    int n,k;
    string ret;
    Solution S;
    while(cin>>n>>k)
    {
       ret = S.getPermutation(n,k);
       if(ret.size()) cout<<ret<<endl;
       else cout<<"NULL"<<endl;
    }
    return 0;
}

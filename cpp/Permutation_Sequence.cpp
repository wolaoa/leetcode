#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> fac;
    string getPermutation(int n, int k) {
       string src,des;

       fac.resize(10,1);
       for(int i=2;i<=n;i++) fac[i] = fac[i-1]*i;

       if(k>fac[n]) return des;
       for(int m=1;m<=n;m++) src+=('0'+m);  //Ô´×Ö·û´®³õÊ¼»¯

       k--;
       for(int j=n;j>1;j--)
       {
           if(k>=fac[j-1])
           {
              int temp = k/fac[j-1];
              k%=fac[j-1];
              des+=src[temp];
              src.erase(temp,1);
           }
           else
           {
              des+=src[0];
              src.erase(0,1);
           }
       }
       des+=src[0];
       return des;
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

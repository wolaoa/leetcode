#include <iostream>
#include <map>
#include <vector>
using namespace std;


    vector<int> twosum(vector<int> &numbers, int target){
          map<int ,int> match;
          vector<int> ans;
          ans.clear();
          int i;
          for(i=0;i<numbers.size();i++)
              match[numbers[i]] = i+1;
          for(i=0;i<numbers.size();i++)
          {

               if(match.find(target - numbers[i]) != match.end()  && i+1 != match[target - numbers[i]])
               {
                   ans.push_back(i+1);
                   ans.push_back(match[target-numbers[i]]);
                   break;
               }
          }
          return ans;
    }

int main()
{
    vector<int> vi,ans;
    int n,target,a;
    while(cin>>n>>target)
    {
        vi.clear();
        for(int i=0;i<n;i++)
        {
            cin>>a;
            vi.push_back(a);
        }
        ans = twosum(vi,target);
        if(ans.size()) cout<<ans[0] <<ans[1]<<endl;
    }
    return 0;
}

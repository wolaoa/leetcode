#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
private:
    vector<int> ans;
    vector<vector<int> > ret;
public:
    void DFS(int start,vector<int> &candidates, int target){
        if(target==0){
            ret.push_back(ans);
            return;
        }

        for(int i=start;i<candidates.size();++i){
            if(target <candidates[i]) return;
            ans.push_back(candidates[i]);
            DFS(i,candidates,target-candidates[i]);
            ans.pop_back();
        }
    }
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        ans.clear();
        ret.clear();
        if(!target || !candidates.size()) return ret;
        sort(candidates.begin(),candidates.end());
        DFS(0,candidates,target);
        return ret;
    }
    void print(vector<vector<int> > result){
        if(!result.size()) return;
        for(int i=0;i<result.size();i++){
            for(int j=0;j<result[i].size();j++){
                cout<<result[i][j]<<" ";
            }
            cout<<endl;
        }
    }
};

int main(){
    vector<int> candidates;
    int target,n,num;
    Solution S;
    while(cin>>target>>n){
        candidates.clear();
        for(int i=0;i<n;i++){
            cin>>num;
            candidates.push_back(num);
        }
        S.print(S.combinationSum(candidates,target));
    }
    return 0;
}

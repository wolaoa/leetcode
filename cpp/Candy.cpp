#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int candy(vector<int> &ratings) {
        int len = ratings.size();
        if(len<=1) return len;
        int i,tot=0;
        vector<int> up(len,1);
        vector<int> down(len,1);
        for(i=1;i<len;i++)
            if(ratings[i]>ratings[i-1]) up[i] = up[i-1]+1;
        for(i=len-2;i>=0;i--)
            if(ratings[i]>ratings[i+1]) down[i]= down[i+1]+1;
        for(i=0;i<len;i++){
            tot += max(up[i],down[i]);
        }
        return tot;
    }
};

int main()
{
    vector<int> ratings;
    int n,num;
    Solution S;
    while(cin>>n){
        ratings.clear();
        for(int i=0;i<n;i++){
            cin>>num;
            ratings.push_back(num);
        }
        cout<<S.candy(ratings)<<endl;
    }
    return 0;
}

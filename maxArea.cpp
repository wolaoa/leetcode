#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int ans=0,left=0,right=height.size()-1,contain;
        while(left<right)
        {
            contain = (right-left)*min(height[right],height[left]);
            ans = max(contain, ans);
            height[left]<=height[right]?left++:right--;
        }
        return ans;
    }
};

int main()
{
    vector<int> height;
    int n,num;
    Solution s;
    while(cin>>n)
    {
        height.clear();
       for(int i=0;i<n;i++)
       {
            cin>>num;
            height.push_back(num);
       }
       cout<<s.maxArea(height)<<endl;
    }
    return 0;
}

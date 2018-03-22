#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    int jump(int A[], int n){
        if(n==1) return 0;
        int step=0;
        int left=0,right=A[0],pre_right;
        while(left<=right)
        {
            ++step;
            pre_right  = right;
            if(right>=n-1) return step;
            for(int j=left;j<=pre_right;j++)
               right = max(right,j+A[j]);
            left = pre_right+1;
        }
        return 0;
    }
};

int main()
{
    Solution s;
    int A[1000],n;
    while(cin>>n)
    {
        for(int i=0;i<n;i++) cin>>A[i];
        cout<<s.jump(A,n)<<endl;
    }
    return 0;
}

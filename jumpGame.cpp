#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    bool canJump(int A[], int n){
        vector<int> remain(n,0);
        remain[0]=0;
        for(int i=1;i<n;i++)
        {
            remain[i] = max(remain[i-1],A[i-1])-1;
            if(remain[i]<0) return false;
        }
        return remain[n-1]>=0;
    }
    bool canJump1(int A[], int n){
        int reach=0;
        for(int i=0;i<n;i++)
        {
            if(i>reach) return false;  // i unreachable
            int temp = i+A[i];       // current maxmum reach point
            if(temp>reach) reach = temp;
        }
        return reach>=(n-1);
    }
};

int main()
{
    Solution s;
    int A[1000],n;
    while(cin>>n)
    {
        for(int i=0;i<n;i++) cin>>A[i];
        if(s.canJump(A,n))cout<<"canJump Yes"<<endl;
        else  cout<<"canJump No"<<endl;

        if(s.canJump1(A,n)) cout<<"canJump1 Yes"<<endl;
        else  cout<<"canJump1 No"<<endl;

    }
    return 0;
}

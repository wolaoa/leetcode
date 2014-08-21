#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int> > vi(n,vector<int>(n));
        int len = n/2;
        int count=1;
        int i,j;
        for(i=0;i<len;i++)
        {
            for(j=i;j<n-i;j++) vi[i][j]=count++;
            for(j=i+1;j<n-i;j++) vi[j][n-i-1] = count++;
            for(j=n-i-2;j>=i;j--) vi[n-i-1][j] =count++;
            for(j=n-i-2;j>i;j--) vi[j][i] = count++;
        }
        if(n%2) vi[len][len]=n*n;
        return vi;
    }
};

int main()
{
    int n;
    Solution S;
    while(cin>>n)
    {
        vector< vector<int> > vi(n,vector<int>(n));
        vi = S.generateMatrix(n);
        for(int i=0;i<vi.size();i++)
        {
            for(int j= 0;j<vi[0].size();j++)
                cout<<vi[i][j]<<" ";
            cout<<endl;
        }
    }
    return 0;
}

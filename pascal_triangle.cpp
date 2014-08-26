#include <iostream>
#include <vector>
using namespace std;

    vector<vector<int> > generate(int numRows) {
        vector<int> vi;
        vector<vector<int> > ans;
        int i,j;
        vi.push_back(1);
        ans.clear();

        if(numRows<=0)
            return ans;
        if(1==numRows)
        {
            ans.push_back(vi);
            return ans;
        }
        if(2==numRows)
        {
            ans.push_back(vi);
            vi.push_back(1);
            ans.push_back(vi);
            return ans;
        }

        ans.push_back(vi);
        vi.push_back(1);
        ans.push_back(vi);
        for(i=2;i<numRows;i++)
        {
            vi.clear();
            vi.push_back(1);
            for(j=1;j<i;j++)
            {
                vi.push_back(ans[i-1][j-1]+ans[i-1][j]);
            }
            vi.push_back(1);
            ans.push_back(vi);
        }
        return ans;
    }

int main()
{
    vector<vector<int> > triangle;
    int n,i,j;
    while(cin>>n)
    {
        triangle = generate(n);
        for(i=0;i<n;i++)
        {
            for(j=0;j<=i;j++)
                cout<<triangle[i][j]<<" ";
            cout<<endl;
        }
    }
    return 0;
}

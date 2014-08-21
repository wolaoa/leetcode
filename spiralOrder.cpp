#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int> > &matrix) {
        vector<int> vi;
        vi.clear();



        int rows= matrix.size();
        if(rows==0) return vi;
        int lines = matrix[0].size();
        if(lines==0) return vi;

        vector<vector<int> > mark(rows,vector<int>(lines));

        int i=0,j=0,k=0;
        while(i<=rows/2 && j<=lines/2)
        {
            if(mark[i][j]==1) break;
            for(k=j;k<lines && mark[i][k]==0;k++)
            {
                vi.push_back(matrix[i][k]);
                mark[i][k]=1;
            }
            finish = k;
            for(k=i+1;k<rows && mark[lines-j-1][k]==0; k++)
            {
                vi.push_back(matrix[lines-j-1][k]);
                mark[k][lines-j-1]=1;
            }
            for(k=lines-j-2;k>=j && mark[rows-i-2][k]==0;k--)
            {
                vi.push_back(matrix[rows-i-2][k]);
                mark[rows-i-2][k]=1;
            }
            for(k=rows-i-2;k>i && !mark[k][j];k--)
            {
                vi.push_back(matrix[k][j]);
                mark[k][j]=1;
            }
            j++;
        }
        return vi;
    }
};

int main()
{
    int n,m,num;
    Solution S;
    while(cin>>n>>m)
    {
        vector<vector<int> > vi(n, vector<int>(m));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>num;
                vi[i][j]=num;
            }
        }
        vector<int> v = S.spiralOrder(vi);
        for(int k=0;k<v.size();k++) cout<<v[k]<<" ";
        cout<<endl;
    }
    return 0;
}

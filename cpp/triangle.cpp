#include <iostream>
#include <vector>
using namespace std;

int minimumTotal(vector<vector<int> > & triangle)
{
    vector<int> vi;
    int len = triangle.size();
    if(1==len) return triangle[0][0];

    int i,j;
    for(i=len-2;i>=0;--i)
    {
        for(j=0;j<triangle[i].size();j++)
        {
            triangle[i][j]+= (triangle[i+1][j]<triangle[i+1][j+1]?triangle[i+1][j]:triangle[i+1][j+1]);
        }
    }
    return triangle[0][0];
}

int main()
{
    vector<int> vi;
    vector<vector<int> > triangle;
    int n,a;
    while(cin>>n)
    {
        triangle.clear();
        for(int i=0;i<n;i++)
        {
            vi.clear();
            for(int j=0;j<=i;j++)
            {
                cin>>a;
                vi.push_back(a);
            }
            triangle.push_back(vi);
        }
        cout<<minimumTotal(triangle)<<endl;
    }
    return 0;
}

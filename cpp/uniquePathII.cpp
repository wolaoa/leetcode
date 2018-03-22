#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid){
        height = obstacleGrid.size();
        weight = obstacleGrid[0].size();
        if(obstacleGrid[0][0]==1 || obstacleGrid[height-1][weight-1]==1)
            return 0;
        tmp = vector<vector<int> >(height+1, vector<int>(weight+1,0));
        tmp[0][0]=1;
        for(i=1;i<=height;i++)
        {
            for(int j=1;j<weight;j++)
            {
                if(obstacleGrid[i-1][j]!=1 && obstacleGrid[i][j-1]!=1)
            }
        }
        return  D
    }
private:
    int height;
    int weight;
    vector<vector<int> > tmp;
};

int main()
{
    Solution S;
    vector<vector<int> > obsGrid;
    vector<int> vi;
    int n,m,num;
    while(cin>>n>>m)
    {
        obsGrid.clear();
        for(int i=0;i<n;i++)
        {
            vi.clear();
            for(int j=0;j<m;j++)
            {
                cin>>num;
                vi.push_back(num);
            }
            obsGrid.push_back(vi);
        }
        cout<<S.uniquePathsWithObstacles(obsGrid)<<endl;
    }
    return 0;
}

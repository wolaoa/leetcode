#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid){
        height = obstacleGrid.size();
        weight = obstacleGrid[0].size();
        return  DFS(0,0,obstacleGrid);
    }
private:
    int height;
    int weight;
    int DFS(int x,int y,vector<vector<int> > &obstacleGrid){
        if(x == height-1 && y == weight-1) return 1;
        if(x == height || y == weight) return 0;
        if(obstacleGrid[x][y]==1) return 0;
        return DFS(x+1,y,obstacleGrid)+DFS(x,y+1,obstacleGrid);
    }
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

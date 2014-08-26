#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int rows = matrix.size();
        int lines= matrix[0].size();
        int i=0,j=lines-1;
        while(i<rows && j>=0)
        {
            if(target==matrix[i][j]) return true;
            else if(target>matrix[i][j]) i++;
            else  j--;
        }
        return false;
    }
};

int main()
{
    vector<vector<int> > matrix;
    int m,n,num,target;
    vector<int> temp;
    Solution S;
    while(cin>>m>>n>>target)
    {
        matrix.clear();
        for(int i=0;i<m;i++)
        {
            temp.clear();
            for(int j=0;j<n;j++)
            {
                cin>>num;
                temp.push_back(num);
            }
            matrix.push_back(temp);
        }
        if(S.searchMatrix(matrix,target)) cout<<"Yes"<<endl;
        else   cout<<"No"<<endl;
    }
    return 0;
}

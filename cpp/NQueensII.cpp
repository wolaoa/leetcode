#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> vi;
    vector<int> mark;
    int length;
    int count;
    void DFS(int len)
    {
        if(len == length)
        {
            count++;
            return;
        }
        for(int i=0;i<length;i++)
        {
            if(mark[i]==1)
            {
//                vi[len]=i;
                  mark[i]=0;
                  DFS(len+1);
                  mark[i]=1;
            }
        }
    }
    int totalNQueens(int n) {
        if(n<=1) return n;
        length=n;
        count=0;
        vi.resize(n);
        mark.assign(n,1);
        DFS(0);
        return count;
    }
};
int main()
{
    int n;
    Solution S;
    while(cin>>n)
        cout<<S.totalNQueens(n)<<endl;
    return 0;
}

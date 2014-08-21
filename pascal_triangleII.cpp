#include <iostream>
#include <vector>
using namespace std;


    vector<int> getRow(int rowIndex) {
        vector<int> vi;
        vi.push_back(1);

        if(rowIndex==0) return vi;

        int i,j;
        for(i=1;i<=rowIndex;i++)
        {
            vi.push_back(1);
            for(j=vi.size()-2;j>=1;j--)
            {
                vi[j] += vi[j-1];
            }
        }
        return vi;
    }

    int main()
    {
        int n;
        vector<int> ans;
        while(cin>>n)
        {
            ans = getRow(n);
            for(int i=0;i<ans.size();i++)
                cout<<ans[i]<< " ";
            cout<<endl;
        }
        return 0;
    }

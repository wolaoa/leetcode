#include <iostream>
#include <vector>
using namespace std;

    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int station = gas.size();
        int i,sum=0,start=0,total=0;
        
        for(i=0;i<station;i++)
            gas[i]-=cost[i];
        
        for(i=0;i<station;i++) total+=gas[i];
        if(total<0) return -1;
        
        for(i=0;i<station;i++)
        {
              sum+= gas[i];
              if(sum<0)
              {
                  start=i;
                  sum=0;
              }
        }
        return start+1;
        
    }
    
    int main()
    {
        vector<int> gas,cost;
        int n,i,a,j;
        while(cin>>n)
        {
           gas.clear();
           cost.clear();
           for(i=0;i<n;i++)
           {
             cin>>a;
             gas.push_back(a);
           }
           for(j=0;j<n;j++)
           {
             cin>>a;
             cost.push_back(a);
           }
           cout<<canCompleteCircuit(gas,cost)<<endl;
        }
        return 0;
    }

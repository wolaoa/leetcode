#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

    vector<vector<int> > threeSum(vector<int> &num) {
          int a,b,c,len,i;
          sort(num.begin(),num.end());
          len =num.size();

          
          vector< vector<int> > vi;
          vi.clear();
          for(i=0;i<len;i++)
          {
               a = num[i];
               if(a>0) break;
               b = i+1;
               c = len-1;
               while(b<c)
               {
                  if(num[b]+num[c]+a ==0)
                  {
                      vector<int> tmp;
                      tmp.push_back(a);
                      tmp.push_back(num[b]);
                      tmp.push_back(num[c]);
                      c--;
                      vi.push_back(tmp);            
                  }
                  else if(num[b]+num[c]+ a>0)
                  {
                       c--;
                  }
                  else
                  {
                      b++;
                  }
               }
          }
          return vi;        
    }
    
int main()
{
    vector< vector<int> > vi;
    vector<int> src;
    int n,i,num,j;
    while(cin>>n)
    {
       for(i=0;i<n;i++)
       {
          cin>>num;
          src.push_back(num);
       }
       cout<<"------------"<<endl;
       vi = threeSum(src);
       for(i=0;i<vi.size();i++)
       {
          for(j=0;j<vi.front().size();j++)
            cout<<vi[i][j]<<" ";
          cout<<endl;
       }
    }
    return 0;
}

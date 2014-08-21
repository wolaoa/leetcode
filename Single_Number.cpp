  #include <iostream>
  #include <set>
  using namespace std;
  int singleNumber(int A[], int n) {
        int i=0,total=0,sum=0;
        set<int> si;
        si.clear();
        for(i=0;i<n;i++)
        {
            total+=A[i];
            if(si.find(A[i])==si.end()) si.insert(A[i]);
        }
        set<int>::iterator iter;
        for(iter=si.begin();iter!=si.end();iter++)
           sum+=*iter;
        return 2*sum-total;
  }
    
int main()
{
    int  A[10000],n;
    while(cin>>n)
    {
      for(int i=0;i<n;i++)
        cin>>A[i];
      cout<<singleNumber(A,n)<<endl; 
    }
    return 0;
} 

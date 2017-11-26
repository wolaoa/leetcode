#include <iostream>
#include <string>
using namespace std;

string convert(string s,int nRows)
{
       if(nRows==1) return s;
       cout<<s<<" "<<nRows<<endl;
       cout<<s.size()<<endl;
       int i=0,j=0,Count=0;
       string a[nRows],b;
       for(i=0;i<nRows;i++)
          a[i].clear();
       b.clear();
       int time = s.size()/2/(nRows-1);
       int remain = s.size()%(2*(nRows-1));
       while(time--)
       {
          for(i=0;i<nRows;i++)
             a[i]+=s[Count++];
          for(i=nRows-2;i>=1;i--)
             a[i]+=s[Count++];
        }
        if(remain<=nRows)
        {
           for(i=0;i<remain;i++)
             a[i]+=s[Count++];
        }
        else
        {
            for(i=0;i<nRows;i++)
              a[i]+=s[Count++];
            remain-=nRows;
            i=nRows-2;
            for(j=0;j<remain;j++)
               a[i--] += s[Count++];
        }
        for(i=0;i<nRows;i++)
           b+=a[i];
        return b;
}

int main()
{
    string a;
    int nRows;
    while(cin>>a>>nRows)
       cout<<convert(a,nRows)<<endl;
    return 0;
}

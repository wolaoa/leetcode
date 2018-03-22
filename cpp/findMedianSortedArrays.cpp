#include<iostream>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int length = m+n+1;
        int l1 = length/2;
        int l2 = length-l1-1;
        int Aleft=0,Aright=m-1,Bleft=0,Bright=n-1;

        while(!(Aleft>Bright || Aright>Bleft) && Aleft<=Aright && Bleft<=Bright)
        {
            int Amedian = (Aleft+Aright)/2;
            int Bmedian = (Bleft+Bright)/2;
            if(A[Amedian]<B[Bmedian])
            {
                l1-= Amedian-Aleft;
                l2-= Bright-Bmedian;
                Aleft = Amedian+1;
                Bright = Bmedian;
            }
            else if(A[Amedian]>B[Bmedian])
            {
                l1-= Bmedian-Bleft;
                l2-= Aright-Amedian;
                Aright = Amedian;
                Bleft = Bmedian+1;
            }
            else
                return A[Amedian];
        }
        if(Aleft>Bright)
        {
            if(Aleft-Aright > l1)
               return A[Aleft+l1];
            else
               return B[Bleft+l1-Aleft+Aright];
        }
        if(Bleft>Aright)
        {
            if(Bleft-Bright > l1)
               return B[Bleft+l1];
            else
               return A[Aleft+l1-Bleft+Bright];
        }
    }
};

int main()
{
    Solution s;
    int m,n,A[100],B[100];
    int i,j;
    while(cin>>m>>n)
    {
        for(i=0;i<m;i++) cin>>A[i];
        for(j=0;j<n;j++) cin>>B[j];
        cout<<s.findMedianSortedArrays(A,m,B,n)<<endl;
    }
    return 0;
}

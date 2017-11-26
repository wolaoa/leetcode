#include<iostream>
#include <vector>

using namespace std;
vector<int> searchRange(int A[], int n, int target) {
    int left = 0,left1;
    int right = n-1,right1;
    int middle;
    vector<int> vi;
    vi.clear();

    while(left<=right)
    {
        middle = left + ((right - left)>>1);
        if(A[middle]==target)
            break;
        else if(A[middle]>target)
            right = middle-1;
        else
            left = middle+1;
    }
    if(left > right)
    {
        left=right=-1;
    }
    else
    {
        if(A[0]==target)
            left=0;
        if(A[n-1]==target)
            right=n-1;

        right1=middle;
        left1=middle;
        while(left<right1)
        {
            if(A[left]==target)
                break;
            middle = ((right1-left)>>1) + left;
            if(A[middle]!=target)
                left = middle+1;
            else
                right1 = middle;
        }
        while(left1<right)
        {
            if(A[right]==target)
                break;
            middle = right+left1;
            middle = (middle%2?(middle+1)/2:middle/2);

            if(A[middle]!=target)
                right = middle-1;
            else
                left1 = middle;
        }
    }
    vi.push_back(left);
    vi.push_back(right);
    return vi;
}

int main()
{
    int A[1000];
    int n,target,i;
    vector<int> vi;
    while(cin>>n>>target)
    {
        for(i=0;i<n;i++)
           cin>>A[i];

        vi.clear();
        vi = searchRange(A,n,target);
        cout<<vi[0]<<" "<<vi[1]<<endl;
    }
    return 0;
}

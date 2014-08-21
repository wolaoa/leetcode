    #include <iostream>
    #include <vector>
    #include <cmath>
    using namespace std;
    
    vector<int> grayCode(int n) {
        int len = pow(2.0,n),i,a;
        vector<int> vi;
        for(i=0;i<len;i++)
        {
            a= i^(i>>1);
            vi.push_back(a);
        }
        return vi;
    }
    
    int main()
    {
        int n;
        vector<int> vi;
        while(cin>>n)
        {
           vi = grayCode(n);
           vector<int>::iterator iter;
           for(iter=vi.begin();iter!=vi.end();iter++)
           cout<<*iter<<" ";
           cout<<endl;
        }
        return 0;

    }

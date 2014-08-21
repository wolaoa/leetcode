 #include <iostream>
 #include <algorithm>
 #include <string>
 using namespace std;

    string addBinary(string a, string b) {
        string c;
        c.clear();
        int len = max(a.size(),b.size()),i,j,ca;

        if(b.size()==0) return a;

        for(i=0;i<=len;i++) c+='0';

        for(i=len,j=a.size()-1;i>=0 && j>=0;i--,j--)
            c[i]+=(a[j]-'0');

        ca=0;
        for(i=len,j=b.size()-1;i>=0 && j>=0;i--,j--)
        {
            char tmp = c[i] + (b[j]-'0')+ca;
            switch(tmp)
            {
            case '0':
                c[i]='0';
                ca=0;
                break;
            case '1':
                c[i]='1';
                ca=0;
                break;
            case '2':
                c[i]='0';
                ca=1;
                break;
            case '3':
                c[i]='1';
                ca=1;
                break;
            }
        }
        while(ca!=0)
        {
            char tmp = c[i]+ca;
            if(tmp == '2')
            {
                c[i]='0';
                ca =1;
            }
            else
            {
                c[i]=tmp;
                ca=0;
            }
            i--;
        }

        if(c[0]=='0') c.erase(0,1);
        return c;
    }

int main()
{
    string a,b;
    while(cin>>a>>b)
        cout<<addBinary(a,b)<<endl;
    return 0;
}

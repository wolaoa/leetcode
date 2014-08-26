 #include <iostream>
 #include <map>
 using namespace std;

    int romanToInt(string s) {
        int ans=0,i;
        map<char,int> Ma;
        {
            Ma['I']=1;
            Ma['V']=5;
            Ma['X']=10;
            Ma['L']=50;
            Ma['C']=100;
            Ma['D']=500;
            Ma['M']=1000;
        }
        ans = Ma[s[0]];
        for(i=1;i<s.size();i++)
        {
            ans = ans + Ma[s[i]];
            if(Ma[s[i]] > Ma[s[i-1]] )
                ans -= 2* Ma[s[i-1]];
        }
        return ans;
    }

    int main()
    {
        string s;
        while(cin>>s)
            cout<<romanToInt(s)<<endl;
        return 0;
    }

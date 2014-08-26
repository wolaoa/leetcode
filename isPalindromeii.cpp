#include<iostream>
#include <string>
#include <cstring>
#include <cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s){
        int left=0,right =s.size()-1;
        while(left<right)
        {
            if(!isalnum(s[left]))
                left++;
            else if(!isalnum(s[right]))
                right--;
            else
            {
                if(tolower(s[left])==tolower(s[right]))
                {
                    left++;
                    right--;
                }
                else
                    return false;
            }
        }
        return true;
    }
};

int main()
{
    Solution s;
    string a;
    while(getline(cin,a))
    {
        if(s.isPalindrome(a)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}

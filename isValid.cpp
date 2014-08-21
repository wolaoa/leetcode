#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        if(s.size()<=1 || s.size()%2) return false;

        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]=='[' || s[i]=='{') st.push(s[i]);
            else if(st.empty())
            {
                return false;
            }
            else
            {
                if(  (s[i]==')' && st.top()=='(') ||
                     (s[i]==']' && st.top()=='[') ||
                     (s[i]=='}' && st.top()=='{') )
                     st.pop();
                else
                    return false;
            }
        }
        if(!st.empty()) return false;
        else return true;
    }
};

int main()
{
    string s;
    Solution Sol;
    while(cin>>s)
    {
        if(Sol.isValid(s)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}

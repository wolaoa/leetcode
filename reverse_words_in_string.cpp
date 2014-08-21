#include <string>
#include <iostream>
using namespace std;
void reverseWords(string &s) {
    string b;
    b.clear();
    
    int i,j,mark;
    
    i=0;
    // erase pre spaces
    while(i<s.size()-1 && s[i]==' ') i++;
    s = s.substr(i);
    
    // omit tail spaces
    i=s.size()-1;
    while(i>=0 && s[i]==' ' ) i--;
    j=i;

    mark=0;
    while(i>=0)
    {       

       while(i>=0 && s[i]!=' ') i--;
       b+= s.substr(i+1,j-i);
       j=i;
       
       while(i>=0 && s[i]==' ')
       {
           mark=1;
           j--;
           i--;
       }
       if(mark)
       { 
            b+=" ";
            mark=0;
       }
       if(i<0)
         break;
    }
    
    cout<<b<<"1"<<endl;      
}

int main()
{
    string a;
    while(getline(cin,a)) 
       reverseWords(a);
    return 0;
}

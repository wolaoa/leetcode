#include <iostream>
#include <cstring>
using namespace std;

    bool isNumber(char s[]) {
         int i=0,len=strlen(s);
         while(s[len-1]==' ') len--;
         while(s[i]==' ') i++;
         
         
         if(len==1)
         {
            if(s[0]>='0' && s[0]<='9') return true;
            else  return false;
         }
         else
         {
             if(s[i]=='+' || s[i]=='-' || (s[i]>='0' && s[i]<='9'))
             {
                  i++;
                  if(s[i]=='E' || s[i]=='e') return false;
                  
                  while(i<len && s[i]>='0' && s[i]<='9') i++;
                  if(i==len) return true;
                  
                  if(s[i]=='e' || s[i]=='E')
                  {
                      i++;
                      if(i==len) return false;
                      else
                      {
                            while(i<len && s[i]>='0' && s[i]<='9') i++;
                            if(i== len) return true;
                            else return false;
                      }
                  }
                  else if(s[i]=='.')
                  {
                      i++;
                      if(i==len) return false;
                      else
                      {
                          while(i<len && s[i]>='0' && s[i]<='9') i++;
                          if(i== len) return true;
                          if(s[i]=='e' || s[i]=='E')
                          {
                              i++;
                              if(i==len) return false;
                              else
                              {
                                    while(i<len && s[i]>='0' && s[i]<='9') i++;
                                    if(i== len) return true;
                                    else return false;
                              }
                          }
                          else
                              return false;
                      }
                       
                  }
                  else return false;        
             }
             else
                 return false;
         }
    }
    
    int main()
    {
        char a[100];
        while(cin>>a)
        {
           if(isNumber(a)) cout<<"Yes"<<endl;
           else cout<<"No"<<endl;
        }
        return 0;
    }

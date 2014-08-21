 #include <iostream>
 #include <map>
 using namespace std;

/*    string intToRoman(int num) {
        string ans;
        while(num>0)
        {
            if(num>=1000)
            {
                ans+="M";
                num-=1000;
            }
            else if(num>=900)
            {
                ans+="CM";
                num-=900;
            }
            else if(num>=500)
            {
                ans+="D";
                num-=500;
            }
            else if(num>=400)
            {
                ans+="CD";
                num-=400;
            }
            else if(num>=100)
            {
                ans+="C";
                num-=100;
            }
            else if(num>=90)
            {
                ans+="XC";
                num-=90;
            }
            else if(num>=50)
            {
                ans+="L";
                num-=50;
            }
            else if(num>=40)
            {
                ans+="XL";
                num-=40;
            }
            else if(num>=10)
            {
                ans+="X";
                num-=10;
            }
            else if(num>=9)
            {
                ans+="IX";
                num-=9;
            }
            else if(num>=5)
            {
                ans+="V";
                num-=5;
            }
            else if(num>=4)
            {
                ans+="IV";
                num-=4;
            }
            else
            {
                ans+="I";
                num-=1;
            }
        }
        return ans;
    } */
    string intToRoman(int num) {
        string s[]={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int n[]={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        string ans;
        int i=0;
        while(num>0)
        {
            if(num>=n[i])
            {
                num-=n[i];
                ans+= s[i];
            }
            else
             i++;
        }
        return ans;
    }

    int main()
    {
        int s;
        while(cin>>s)
            cout<<intToRoman(s)<<endl;
        return 0;
    }

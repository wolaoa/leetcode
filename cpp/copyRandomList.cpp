#include <iostream>
using namespace std;

struct RandomList{
       int label;
       RandomListNode *next,*random;
       RandomListNode(int x):label(x),next(NULL),random(NULL){}
};

class Solution{
public:
       RandomListNode *copyRandomListNode(RandomListNode* root){
             RandomListNode ans(0);
             ans->next = root; 
       }
};

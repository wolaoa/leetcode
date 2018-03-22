#include<iostream>
using namespace std;


  struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    ListNode *createList(int n)
    {
        ListNode *l1 = new ListNode(0);
        int num;
        if(n==0) return NULL;
        else
        {
            cin>>num;
            l1->val=num;
            l1->next = createList(--n);
        }
        return l1;
    }
    ListNode *add(ListNode *l1, ListNode *l2,int c)
    {
        ListNode *head= new ListNode(0);
        if(l1==NULL && l2==NULL)
        {
            if(c==0)
               return NULL;
            else
            {
                head->val=1;
               return head;
            }
        }
        if(l1==NULL)
            return add(head,l2,c);
        if(l2==NULL)
            return add(l1,head,c);

        if(l1!=NULL && l2!=NULL)
        {
           head->val =(l1->val + l2->val +c)%10;
           c = (l1->val + l2->val +c)/10;
           head->next = add(l1->next,l2->next,c);
        }
        return head;
    }
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int c=0;
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;

        ListNode *head = add(l1,l2,c);
        return head;
    }
};

int main()
{
    Solution s;
    ListNode *l1,*l2,*ans;
    int n,m;
    while(cin>>n>>m)
    {
        l1 = s.createList(n);
        l2 = s.createList(m);
        ans = s.addTwoNumbers(l1,l2);
        while(ans!=NULL)
        {
            cout<<ans->val<<" ";
            ans= ans->next;
        }
    }
    return 0;

}

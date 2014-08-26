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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode *pre,*first,*last;
        ListNode ans(0);
        pre=first=last=head;
        ans.next=pre;
        for(int i=0;i<n;i++)
            first=first->next; //find faster pointer

        while(first!=NULL)
        {
            first=first->next;
            pre = last;
            last=last->next;
        }
        pre->next = last->next;
        if(last==head) return head->next;
        else return ans.next;
    }
};

int main()
{
    Solution s;
    ListNode *l1,*ans;
    int n,m;
    while(cin>>n>>m)
    {
        l1 = s.createList(n);
        ans= s.removeNthFromEnd(l1,m);
        while(ans!=NULL)
        {
            cout<<ans->val<<" ";
            ans= ans->next;
        }
        cout<<endl;
    }
    return 0;

}


#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* createList(int len)
    {
        if(len==0) return NULL;
        int num;
        cin>>num;
        ListNode *ans = new ListNode(num);
        ans->next=createList(len-1);
        return ans;
    }
    ListNode *partition(ListNode *head, int x) {
        if(head==NULL || head->next==NULL) return head;

        ListNode *lower = new ListNode(-1);
        ListNode *higher = new ListNode(-1);
        ListNode *ltail = lower;
        ListNode *htail = higher;
        ListNode *tmp = head;
        while(tmp){
            if(tmp->val < x){
                ltail->next = tmp;
                ltail = ltail->next;
            }else{
                htail->next = tmp;
                htail = htail->next;
            }
            tmp = tmp->next;
        }
        htail->next=NULL;
        ltail->next=higher->next;
        return lower->next;
    }
    void printList(ListNode *head){
        ListNode *tmp=head;
        while(tmp){
            cout<<tmp->val<<" ";
            tmp=tmp->next;
        }
        cout<<endl;
    }
};

int main()
{
    Solution s;
    int n,x;
    while(cin>>n>>x)
    {
        ListNode *node=s.createList(n),*ans;
        s.printList(node);
        ans = s.partition(node,x);
        s.printList(node);
        s.printList(ans);
    }
    return 0;

}

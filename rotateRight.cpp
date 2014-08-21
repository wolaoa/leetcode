
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
    int getListLength(ListNode *head){
        int len=0;
        ListNode *tmp=head;
        while(tmp){
            len++;
            tmp = tmp->next;
        }
        return len;
    }
    ListNode *rotateRight(ListNode *head, int x) {
        int len = getListLength(head);
        x = x%len;
        if( len<=1 || x==0) return head;

        ListNode *tmp=head;
        ListNode *lend=head;
        ListNode *hstart=head;
        while(tmp->next){
            if(x==0){
                lend = lend->next;
            }else{
                --x;
            }
            tmp = tmp->next;
        }
        hstart = lend->next;
        lend->next=NULL;
        tmp->next=head;
        return hstart;
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
        ans = s.rotateRight(node,x);
        s.printList(ans);
    }
    return 0;

}

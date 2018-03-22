#include <iostream>
using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
    int getListLen(ListNode *head){
        int len=0;
        ListNode *tmp=head;
        while(tmp){len++;tmp=tmp->next;}
        return len;
    }
    ListNode *reverseKGroup(ListNode *head, int k) {
        if(k<=1|| !head || !head->next) return head;
        int len=getListLen(head);
        if(len<k) return head;

        ListNode *pre=new ListNode(0);
        ListNode *change=head;

        for(int j=1;j<=k;j++){
                ListNode *tmp = change;
                change = change->next;
                tmp->next = pre->next;
                pre->next=tmp;
        }
        head->next=reverseKGroup(change,k);
        return pre->next;
    }
    ListNode *createList(int n){
        if(n==0) return NULL;
        int num;
        cin>>num;
        ListNode *head = new ListNode(num);
        head->next = createList(n-1);
        return head;
    }
    void printList(ListNode *head){
        if(!head){
            cout<<endl;
            return;
        }
        cout<<head->val<<" ";
        printList(head->next);
    }
};

int main(){
    Solution S;
    int n,k;
    ListNode *head;
    while(cin>>n>>k){
        head=S.createList(n);
        head=S.reverseKGroup(head,k);
        S.printList(head);
    }
    return 0;
}

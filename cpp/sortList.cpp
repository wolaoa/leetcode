#include<iostream>
using namespace std;
struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
    ListNode *mergeList(ListNode *left,ListNode *right){
        if(left==NULL) return right;
        if(right==NULL) return left;
        ListNode *tmp = new ListNode(0);
        if(left->val <right->val){
            tmp=left;
            left=left->next;
        }else{
            tmp=right;
            right=right->next;
        }
        tmp->next=mergeList(left,right);
        return tmp;
    }
    ListNode *sortList(ListNode *head){
        if(head==NULL || head->next==NULL) return head;
        ListNode *left=head,*right=head->next;
        while(right){
            right = right->next;
            if(right){
                right=right->next;
                left = left->next;
            }
        }
        ListNode *middle = left->next;
        left->next=NULL;
        head = sortList(head);
        middle = sortList(middle);
        head = mergeList(head,middle);
        return head;
    }
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
    ListNode *l1,*ans;
    int n;
    while(cin>>n)
    {
        l1 = s.createList(n);
        l1 = s.sortList(l1);
        s.printList(l1);
    }
    return 0;

}

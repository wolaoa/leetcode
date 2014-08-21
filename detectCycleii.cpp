#include <iostream>
using namespace std;

struct ListNode{
       int val;
       ListNode* next;
       ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
    ListNode *detectCycle(ListNode *head){
        if(head==NULL || head->next==NULL) return head;
        ListNode *startA= head->next;
        ListNode *endA= head->next->next;
        while(endA!=NULL && endA != startA){
            endA=endA->next;
            if(endA){
                endA=endA->next;
                startA=startA->next;
            }
        }
        if(endA==NULL) return NULL;
        cout<<endA->val<<endl;
        if(endA->next == endA) return endA;
        ListNode *match = startA;
        ListNode *start = head;
        while(start!=match){
            start = start->next;
            match = match->next;
        }
        return start;
    }
    ListNode *createList(int len){
        ListNode *root = new ListNode(0);
        ListNode *tmp = root;
        int num;
        for(int i=0;i<len;i++){
            cin>>num;
            tmp->next = new ListNode(num);
            tmp=tmp->next;
        }
        tmp->next = root->next->next->next;
        return root->next;
    }
};

int main(){
    Solution s;
    ListNode *head;
    int num;
    while(cin>>num){
        head = s.createList(num);
        head=s.detectCycle(head);
        cout<<head->val<<endl;
    }
    return 0;
}

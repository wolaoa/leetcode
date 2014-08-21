#include <iostream>
using namespace std;


struct ListNode{
       int val;
       ListNode* next;
       ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
   ListNode* createList(int len){
        int num;
        cin>>num;
        ListNode *ans = new ListNode(0);

        ListNode *head = new ListNode(num);
        ans->next = head;
        for(int i=1;i<len;i++){
            cin>>num;
            ListNode *tmp = new ListNode(num);
            head->next = tmp;
            head = head->next;
        }
        return ans->next;
   }
   void printList(ListNode* head){
        ListNode* tmp = head;
        while(tmp!=NULL){
          cout<<tmp->val<<" ";
          tmp = tmp->next;
        }
        cout<<endl;
   }
    ListNode* reverseList(ListNode* head){
        if(head==NULL || head->next==NULL) return head;
        ListNode *current=head;
        ListNode *ans=NULL;
        while(current){
            ListNode *tmp=current->next;
            current->next = ans;
            ans = current;
            current = tmp;
        }
        return ans;
    }
    ListNode* reorderList(ListNode *head){
        if(head==NULL || head->next==NULL || head->next->next==NULL) return head;

        ListNode *middle,*pre=NULL,*last;
        middle=head; last=head->next;
        while(last){
            last = last->next;
            if(last){
                pre = middle;
				last = last->next;
                middle=middle->next;
            }
        }
        middle=middle->next;
		pre->next->next=NULL;
		middle=reverseList(middle);
        //merge two list
        ListNode *newList=head;
        while(middle){
            ListNode *tmpA = newList->next;
            ListNode *tmpB = middle->next;
            middle->next=tmpA;
            newList->next= middle;
            newList =tmpA;
            middle=tmpB;
        }
        return head;
    }
};

int main(){
    Solution s;
    int n;
    while(cin>>n){
        ListNode *head;
        head = s.createList(n);
        s.printList(s.reorderList(head));
        cout<<endl;
    }
    return 0;
}

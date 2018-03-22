#include <iostream>
#include <vector>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(NULL){}
};

class Solution {
public:
	ListNode *deleteDuplicates(ListNode *head){
		if(head==NULL || head->next==NULL) return head;
		ListNode *pre,*tail;
		pre=head;
		tail=head->next;
		while(tail){
			if(tail->val == pre->val){
				pre->next=tail->next;
			}else{
				pre =pre->next;
			}
			tail=tail->next;
		}
		return head;
	}
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
			cout<<tmp->val<<endl;
			tmp = tmp->next;
		}
	}
};

int main(){
    ListNode *head;
    int len,m,n;
    Solution s;
    while(cin>>len){
			head = s.createList(len);
		s.printList(s.deleteDuplicates(head));
    }
    system("pause");
    return 0;
}

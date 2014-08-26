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
		if(head==NULL || head->next==NULL)return head;
		ListNode *node = head->next;
		if(node->val == head->val){
			while(node && node->val == head->val){
				ListNode *tmp =node;
				node = node->next;
				delete tmp;
			}
			delete head;
			return deleteDuplicates(node);
		}else{
			head->next = deleteDuplicates(head->next);
			return head;
		}
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
		if(head==NULL){
			 cout<<"empty list"<<endl;
			 return;
		}
		ListNode* tmp = head;
		while(tmp!=NULL){
			cout<<tmp->val<<" ";
			tmp = tmp->next;
		}
		cout<<endl;
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

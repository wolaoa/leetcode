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
	ListNode* merge(ListNode* left, ListNode* right){
		if(left==NULL) return right;
		if(right==NULL) return left;
		ListNode *ans =new ListNode(0);
		if(left->val <= right->val){
			ans=left;
			left = left->next;	
		}else{
			ans=right;
			right=right->next;
		}
		ans->next = merge(left,right);
		return ans;
	}
	ListNode* mergesort(vector<ListNode *> &lists,int left,int right){
		if(left>right){
			return NULL;
		}if(left==right){
			return lists[left];
		}else{
			int middle = (left+right)>>1;
			ListNode *lleft = mergesort(lists,left,middle);
			ListNode *lright = mergesort(lists,middle+1,right);
			return merge(lleft,lright);
		}
		
	}
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        int left =0,right =lists.size()-1;
        int middle= (left+right)>>1;
        ListNode *lleft = mergesort(lists,left,middle);
        ListNode *lright = mergesort(lists,middle+1,right);
        return merge(lleft,lright);
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
    vector<ListNode* > vi;
    int len,m,n;
    Solution s;
    while(cin>>len){
		vi.clear();
		for(int i=0;i<len;i++)
		{
			cin>>m;
			head = s.createList(m);
			vi.push_back(head);
		}
		s.printList(s.mergeKLists(vi));
    }
    system("pause");
    return 0;
}

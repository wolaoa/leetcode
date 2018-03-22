#include <iostream>
using namespace std;

struct ListNode{
       int val;
       ListNode* next;
       ListNode(int x):val(x),next(NULL){}
};

class Solution {
public:
	ListNode* insert(ListNode* head,int num){
		ListNode *node = new ListNode(num);
		if(head==NULL || num <=head->val){
			node->next = head;
			return node;
		}
		ListNode *pre = head;
		ListNode *tail = head->next;
		while(tail!=NULL && num > tail->val){
				pre= tail;
				tail=tail->next;
		}
		node->next = pre->next;
		pre->next = node;
		return head;
		
	}
	ListNode* insertionSortList(ListNode *head){
		if(head==NULL || head->next==NULL) return head;
		ListNode *tmp = head;
		ListNode* ans=NULL;
		while(tmp!=NULL){
			ans = insert(ans,tmp->val);
			tmp =tmp->next;
		}
		return ans;
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
        s.printList(s.insertionSortList(head));
    }
    system("pause");
    return 0;
}

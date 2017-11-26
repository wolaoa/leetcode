#include <iostream>
using namespace std;

struct ListNode{
       int val;
       ListNode* next;
       ListNode(int x):val(x),next(NULL){}
};

class Solution{
public:
       ListNode* reverseBetween(ListNode* head,int m,int n){
                 // list length==0 || length==1 || m=n : no need to reverse anthing, just return
                 if(head==NULL || head->next==NULL || m>=n) return head;
                 ListNode *insertPoint=head,*tailStart,*reverseList,*tmp=head;
                 int i=1;
                 while(tmp && i<=n){
                     if(i==m-1){
                          insertPoint = tmp;
                     }else if(i==n){
                          tailStart = tmp->next;
                          break;
                     }
                     tmp = tmp->next;
                     i++;
                 }
                 if(tmp==NULL) return head;
                 if(m==1){
                    reverseList = insertPoint;
                    head = tailStart;
                    for(i=0;i<=n-m;i++){
                        ListNode* node = reverseList;
                        reverseList = reverseList->next;
                        node->next = head;
                        head = node;
                    }   
                 }else{
                    reverseList = insertPoint->next;
                    insertPoint->next = tailStart; // cut down reversed part                    
                    for(i=0;i<=n-m;i++){
                        ListNode* node= reverseList;
                        reverseList = reverseList->next;
                        node->next = insertPoint->next;
                        insertPoint->next = node;
                    }
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
    while(cin>>len>>m>>n){
        head = s.createList(len);
        s.printList(head);
        system("pause");
        s.printList(s.reverseBetween(head,m,n));
    }
    system("pause");
    return 0;
}

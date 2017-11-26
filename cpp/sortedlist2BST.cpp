#include<iostream>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
 };
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    ListNode *getmiddleList(ListNode *left,ListNode *right){
        ListNode *pre,*last;
        pre=left; last =left->next;
        while(last!=right){
            last = last->next;
            if(last!=right){
                last = last->next;
                pre=pre->next;
            }
        }
        return pre;
    }
    TreeNode *getBST(ListNode *left,ListNode *right){
        TreeNode *root = new TreeNode(0);
        if(left==right) return NULL;
        if(left->next == right){
            root->val=left->val;
            return root;
        }
        ListNode *middle =getmiddleList(left,right);
        root->val = middle->val;
        root->left = getBST(left, middle);
        root->right = getBST(middle->next,right);
        return root;
    }
    TreeNode *sortedListToBST(ListNode *head) {
        TreeNode* root= new TreeNode(0);
        if(head==NULL) return NULL;
        if(head->next==NULL){
            root->val=head->val;
            root->left=root->right=NULL;
            return root;
        }
        ListNode *left,*middle,*right;
        middle=left=head;
        right=head->next;
        while(right){
            right=right->next;
            if(right){
                right=right->next;
                middle=middle->next;
            }
        }
        root->val=middle->val;
        root->left = getBST(left, middle);
        root->right= getBST(middle->next,right);
        return root;
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
   void printBST(TreeNode *root){
        TreeNode *tmp =root;
        if(tmp){
            cout<<tmp->val;
            printBST(tmp->left);
            printBST(tmp->right);
        }
   }
};

int main(){
    Solution s;
    int n;
    while(cin>>n){
        ListNode *head;
        head = s.createList(n);
        s.printBST(s.sortedListToBST(head));
        cout<<endl;
    }
    return 0;
}

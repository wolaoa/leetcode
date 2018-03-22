#include<iostream>
#include<string>
#include<cstdlib>
using namespace std;

struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
   TreeNode* createTree(){
        TreeNode* root=new TreeNode(0);
        string num;
        cin>>num;
        if(num == "#"){
            root=NULL;
        }else{
            root->val=atoi(num.c_str());
            root->left = createTree();
            root->right= createTree();
        }
        return root;
   }
   TreeNode* flatten(TreeNode *root){
        if(root==NULL) return NULL;
        flatten(root->left);
        flatten(root->right);
        if(root->left==NULL) return NULL;
        TreeNode *p = root->left;
        while(p->right) p=p->right;
        p->right=root->right;
        root->right=root->left;
        root->left=NULL;
        return root;
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
    while(1){
        TreeNode *head;
        head = s.createTree();
        s.printBST(s.flatten(head));
    }
    return 0;
}

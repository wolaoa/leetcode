#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x):val(x),left(NULL),right(NULL){}
};
class Solution{
public:
    bool isSymmetric(TreeNode *root){
        return root? Symmetric(root->left,root->right):true;
    }
    bool Symmetric(TreeNode *left, TreeNode *right){
        if(!left && !right) return true;
        if(!left || !right) return false;
        return left->val == right->val
            && Symmetric(left->left,right->right)
            && Symmetric(left->right,right->left);
    }
    TreeNode *createTree(){
        string num;
        cin>>num;
        if(num=="#") return NULL;
        else{
            TreeNode *root= new TreeNode(atoi(num.c_str()));
            root->left = createTree();
            root->right= createTree();
            return root;
        }
    }
};

int main(){
    Solution S;
    TreeNode *root;
    while(1){
        root = S.createTree();
        if(S.isSymmetric(root)) cout<<"Yes"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}

/**
  Definition for binary tree */
 #include <vector>
 #include <stack>
 #include <iostream>
 using namespace std;
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };




    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> vi;
        stack<TreeNode*> st;
        if(root!=NULL)
           st.push(root);
        while(!st.empty())
        {
            TreeNode* temp = st.top();
            st.pop();
            vi.push_back(temp->val);
            if(temp->right!=NULL)
                st.push(temp->right);
            if(temp->left!=NULL)
                st.push(temp->left);
        }
        return vi;
    }

int main()
{
    return 0;
}

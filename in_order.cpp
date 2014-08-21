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




    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> vi;
        stack<TreeNode*> st;
        TreeNode *temp=root;
        while(temp!=NULL ||!st.empty())
        {
            while(temp!=NULL)
            {
                st.push(temp);
                temp = temp->left;
            }
            if(!st.empty())
            {
                temp = st.top();
                vi.push_back(temp->val);
                st.pop();
                temp = temp->right;
            }
        }
        return vi;
    }

int main()
{
    return 0;
}

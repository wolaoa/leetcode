#include <iostream>
#include <vector>
using namespace std;

  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
class Solution {
public:
    TreeNode *getValue(int l, int r,vector<int> &num)
    {
        TreeNode * pointer = new TreeNode(0);
        if(l==r)
        {
            pointer->val = num[l];
            pointer->left=pointer->right=NULL;
            return pointer;
        }
        int middle = (l+r)/2;
        pointer->val = num[middle];
        if(l<=middle-1)
            pointer->left = getValue(l,middle-1,num);
        else
            pointer->left=NULL;
        if(middle+1 <= r)
            pointer->right = getValue(middle+1,r,num);
        else
            pointer->right=NULL;
        return pointer;
    }
    TreeNode *sortedArrayToBST(vector<int> &num) {
        int length = num.size();
        if(!length) return NULL;
        TreeNode * head= getValue(0,length-1,num);
        return head;
    }
};

void inorder(TreeNode *head)
{
    if(head!=NULL)
    {
        inorder(head->left);
        cout<<head->val<<" ";
        inorder(head->right);
    }
}
int main()
{
    int n,num;
    vector<int> vi;
    TreeNode * head;
    Solution S;
    while(cin>>n)
    {
        vi.clear();
        for(int i=0;i<n;i++)
        {
            cin>>num;
            vi.push_back(num);
        }
        head = S.sortedArrayToBST(vi);
        inorder(head);
    }
    return 0;
}

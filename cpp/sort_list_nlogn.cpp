#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};


void splitList(ListNode *head, ListNode **left, ListNode **right)
{
    struct ListNode* fast;
    struct ListNode* slow;
    if(head==NULL || head->next==NULL)
    {
        *left = head;
        *right = NULL;
    }
    else
    {
        slow = head;
        fast = head->next;
        
        while(fast!=NULL)
        {
            fast = fast->next;
            if(fast!=NULL)
            {
               fast = fast->next;
               slow = slow->next;
            }
        }
        
        *left = head;
        *right = slow->next;
        slow->next = NULL;
        
    }

}
ListNode* Merge(ListNode* left, ListNode* right)
{
    if(left==NULL)
       return right;
    if(right==NULL)
       return left;
    
    ListNode *temp;
    if(left->val <= right->val)
    {
        temp = left;
        temp->next = Merge(left->next,right);
    }
    else
    {
        temp = right;
        temp->next = Merge(left,right->next);
    }
    return temp;
}

ListNode* sortList(ListNode *head) {
    ListNode *left;
    ListNode *right;
    ListNode *list;
    list = head;
    if(list==NULL || list->next==NULL)
         return NULL;
    splitList(list,&left,&right);
    
    sortList(left);
    sortList(right);
    
    head = Merge(left,right);
}


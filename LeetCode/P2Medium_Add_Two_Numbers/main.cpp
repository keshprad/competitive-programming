// Problem: https://leetcode.com/problems/add-two-numbers/

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode sentNode = ListNode(-1, l1);
    ListNode *prev = &sentNode;

    int carry = 0;
    while (l1 and l2) {
      // put sum in l1
      int total = carry + l1->val + l2->val;
      l1->val = total % 10;
      carry = total / 10;

      // iterate l1, l2
      prev = l1;
      l1 = l1->next;
      l2 = l2->next;
    }

    // attach remaining nodes
    if (l2) {
      prev->next = l2;
    }
    l1 = prev->next;

    while (carry) {
      int total = (l1 ? l1->val : 0) + carry;
      if (!l1) {
        l1 = new ListNode(total % 10);
        prev->next = l1;
      } else {
        l1->val = total % 10;
      }
      carry = total / 10;

      prev = l1;
      l1 = l1->next;
    }

    return sentNode.next;
  }
};
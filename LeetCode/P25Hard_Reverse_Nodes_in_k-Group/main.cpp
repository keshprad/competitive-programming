// Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/
#include <utility>

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
  std::pair<ListNode *, ListNode *> reverse(ListNode *head) {
    ListNode *curr = head, *prev = nullptr;

    while (curr) {
      ListNode *nxt = curr->next;
      curr->next = prev;
      prev = curr;
      curr = nxt;
    }
    return {prev, head};
  }

  ListNode *reverseKGroup(ListNode *head, int k) {
    ListNode sent = ListNode(-1, head), *curr = head, *preced = &sent;

    int c = 1;
    while (curr) {
      if (c == k) {
        ListNode *nxt = curr->next;
        curr->next = nullptr;
        auto [head, tail] = reverse(preced->next);
        tail->next = nxt;
        preced->next = head;
        preced = curr = tail;
        c = 0;
      }

      curr = curr->next;
      c += 1;
    }
    return sent.next;
  }
};
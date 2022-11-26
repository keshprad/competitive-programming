# Problem: https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        # map key to LinkedList node to allow O(1) lookup
        self.cache = {}

        # dummy head and tail nodes
        # use a linkedlist to maintain most recently used items
        # recent on left, least recent on right
        # allows for O(1) add to cache and remove LRU
        self.l = Node(0, 0)
        self.r = Node(0, 0)
        self.l.next = self.r
        self.r.prev = self.l

    # add node to start of linked list next to (self.l)
    def add(self, n):
        prev, nxt = self.l, self.l.next
        prev.next, nxt.prev = n, n
        n.prev, n.next = prev, nxt

    # remove node
    def remove(self, n):
        n.prev.next, n.next.prev = n.next, n.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            # key not in cache
            return -1
        else:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # if key already in list, remove it to update
        if key in self.cache:
            self.remove(self.cache[key])
        # add new val to cache
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        # cache capacity exceeded
        if len(self.cache) > self.size:
            # remove LRU (the rightmost element since elements added to left)
            lru_node = self.r.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

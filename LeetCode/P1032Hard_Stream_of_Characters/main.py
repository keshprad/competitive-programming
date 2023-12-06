# Problem: https://leetcode.com/problems/stream-of-characters/
from typing import List
from collections import defaultdict


class Trie:
    def __init__(self):
        self.root = defaultdict(bool)   # default to False
        self.term = '$'

    def add(self, word):
        node = self.root
        for ch in word:
            if not node[ch]:
                node[ch] = defaultdict(bool)
            node = node[ch]
        node[self.term] = True

    def query_node(self, prefix):
        # query the node for a prefix
        node = self.root
        for ch in prefix:
            if not node[ch]:
                # fall out of trie
                return None
            node = node[ch]
        return node

    def is_sentinel(self, node):
        return node[self.term] if node else False

    def query(self, word):
        # query a word
        node = self.find_node(word)
        return self.is_sentinel(node)


class StreamChecker:
    def __init__(self, words: List[str]):
        # construct trie with all words added backward
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])

        # maintain stream
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        for i in range(len(self.stream)-1, -1, -1):
            suff = self.stream[i:][::-1]
            node = self.trie.query_node(suff)

            if not node:
                # fell out of trie, further suffixes would fail too
                return False
            if self.trie.is_sentinel(node):
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

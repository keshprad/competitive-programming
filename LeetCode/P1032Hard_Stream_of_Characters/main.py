# Problem: https://leetcode.com/problems/stream-of-characters/
from typing import List


class Trie:
    def __init__(self):
        self.edges = {}
        self.is_terminal = False

    def __str__(self):
        return str({k: str(self.edges[k]) for k in self.edges})

    def add(self, word):
        def add(node, word, i):
            if i == len(word):
                # reached terminal
                node.is_terminal = True
                return

            ch = word[i]
            if ch not in node.edges:
                # create edge
                node.edges[ch] = Trie()
            # traverse edge
            add(node.edges[ch], word, i+1)

        add(self, word, 0)

    def query_node(self, prefix, node=None):
        # query the resulting node for a prefix
        def query_node(node, prefix, i):
            if i == len(prefix):
                return node

            ch = prefix[i]
            if ch not in node.edges:
                # fall out of trie
                return None
            # traverse edge
            return query_node(node.edges[ch], prefix, i+1)

        return query_node(node or self, prefix, 0)

    def query(self, word):
        # query a word
        node = self.query_node(word)
        return node.is_terminal


class StreamChecker:
    def __init__(self, words: List[str]):
        # construct trie with all words added backward
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])

        # maintain stream
        self.stream = []

    def query(self, letter: str) -> bool:
        '''
        Time complexity: O(n)
        '''
        self.stream.append(letter)

        node = self.trie
        for i in range(len(self.stream)-1, -1, -1):
            # query character by character to prevent repeated work
            ch = self.stream[i]
            node = node.query_node(ch, node)

            if not node:
                # fell out of trie, further suffixes would fail too
                # "shortcircuit" to False
                return False
            if node.is_terminal:
                # at least one suffix works
                # "shortcircuit" to True
                return True
        # didn't find matching suffixes
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

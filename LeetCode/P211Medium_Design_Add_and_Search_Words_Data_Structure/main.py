from collections import defaultdict
# Problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True

    def search(self, word: str) -> bool:
        def search_word(node: TrieNode, word: str):
            if len(word) == 0:
                return node.is_word

            letter = word[0]
            if letter != '.':
                if letter in node.children:
                    return search_word(node.children[letter], word[1:])
                else:
                    return False
            else:
                return any(search_word(node, word[1:]) for node in node.children.values())

        return search_word(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

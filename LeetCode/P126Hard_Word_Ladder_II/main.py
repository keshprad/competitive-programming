from collections import defaultdict
from typing import List
# Problem: https://leetcode.com/problems/word-ladder-ii/


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        # Early exit case. If endWord cannot be formed
        if endWord not in wordList:
            return []

        # Stores current word & all sequences to get it
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            # Limit alphabet to only letters existing in wordList
            alphabet = {letter for word in wordList for letter in word}
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    # Returns all found sequences
                    return layer[word]
                for i in range(len(word)):
                    for letter in alphabet:
                        new_word = f'{word[:i]}{letter}{word[i+1:]}'
                        if new_word in wordList:
                            # Add new_word to all sequences to create new layer
                            new_layer[new_word] += [
                                seq + [new_word] for seq in layer[word]
                            ]

            # Remove from wordList if the words have already been found
            wordList -= set(new_layer.keys())
            # Use the new layer to continue
            layer = new_layer
        return layer[word]

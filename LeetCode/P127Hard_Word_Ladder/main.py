from collections import deque
from typing import List
# Problem: https://leetcode.com/problems/word-ladder/


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        wordList = set(wordList)
        # Limit alphabet to only letters in wordList
        alphabet = {letter for word in wordList for letter in word}
        queue = deque([[beginWord, 1]])

        # Perform Breadth First Search
        while queue:
            word, ladder_len = queue.popleft()
            # Early exit case
            if word == endWord:
                return ladder_len

            # Try all word combos
            for i in range(len(word)):
                # Try all letters combos at each position
                for letter in alphabet:
                    next_word = f'{word[:i]}{letter}{word[i+1:]}'
                    if next_word in wordList:
                        # Add new ladder step to the queue
                        queue.append([next_word, ladder_len + 1])
                        # Remove next_word from wordList.
                        # Sequence cannot include next_word later, since it would mean a valid shorter sequence exists.
                        wordList.remove(next_word)
        return 0

    # Extending the problem to remember the ladder path as well as length
    def ladderLength_track_ladder(self, beginWord: str, endWord: str,
                                  wordList: List[str]) -> int:
        wordList = set(wordList)
        # Limit alphabet to only letters in wordList
        alphabet = {letter for word in wordList for letter in word}
        queue = deque([[beginWord, beginWord, 1]])

        # Perform Breadth First Search
        while queue:
            word, ladder, ladder_len = queue.popleft()
            # Early exit case
            if word == endWord:
                return ladder, ladder_len

            # Try all word combos
            for i in range(len(word)):
                # Try all letters combos at each position
                for letter in alphabet:
                    next_word = f'{word[:i]}{letter}{word[i+1:]}'
                    if next_word in wordList:
                        # Add new ladder step to the queue
                        queue.append([
                            next_word, f'{ladder} -> {next_word}',
                            ladder_len + 1
                        ])
                        # Remove next_word from wordList.
                        # Sequence cannot include next_word later, since it would mean a valid shorter sequence exists.
                        wordList.remove(next_word)
        return 0

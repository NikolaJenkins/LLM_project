from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        leads = deque()
        leads.append((beginWord, 0))
        allSubs = defaultdict(list)
        length = len(beginWord)
        for word in wordList:
            for index in range(length):
                allSubs[word[:index] + "?" + word[index + 1:]].append(word)
        visited = set()
        while leads:
            next, depth = leads.popleft()
            if next == endWord:
                return depth + 1
            for index in range(length):
                children = allSubs[next[:index] + "?" + next[index + 1:]]
                for child in children:
                    if child not in visited:
                        visited.add(child)
                        leads.append((child, depth + 1))
        return 0



    def filterChildren(self, word: str, wordList: List[str]) -> List[str]:
        children = list()
        otherWords = [x for x in wordList if x != word]
        for mutationIndex in range(len(word)):
            prefix = word[:mutationIndex]
            suffix = word[mutationIndex + 1:]
            for mutatedWord in otherWords:
                mutatedWordPrefix = mutatedWord[:mutationIndex]
                mutatedWordSuffix = mutatedWord[mutationIndex + 1:]
                if prefix == mutatedWordPrefix and suffix == mutatedWordSuffix:
                    children.append(mutatedWord)
        return children

s = Solution()
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
assert 5 == s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
assert 0 == s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
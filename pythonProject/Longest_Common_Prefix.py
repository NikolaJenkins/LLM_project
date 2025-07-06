from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for w in range(1, len(strs)):
            prefix = self.commonPrefix(prefix, strs[w])
            print(prefix)
        return prefix


    def commonPrefix(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        prefix = ""
        for i in range(length):
            if word1[i] == word2[i]:
                prefix = prefix + word1[i]
                # print(prefix)
            else:
                break
        return prefix

s = Solution()

# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# print(s.commonPrefix("flower", "flower"))
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
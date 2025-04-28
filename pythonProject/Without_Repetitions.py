from collections import Counter


class Solution(object):
    def quadraticLengthOfLongestSubstring(self, s):
        maxLength = 0
        for length in range(len(s)):
            for startIndex in range(len(s) - length):
                if length > maxLength:
                    if self.noRepeatingCharacters(s[startIndex: startIndex + length]):
                        maxLength = length
        return maxLength

    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        startIndex = 0
        #stabilized
        endIndex = 0
        maxLength = 0

        #destabilize
        while endIndex < len(s) - 1:
            counter[s[endIndex]] += 1
            while counter[s[endIndex]] > 1:
                counter[s[startIndex]] -= 1
                startIndex += 1
            endIndex += 1
            if endIndex - startIndex > maxLength:
                maxLength = endIndex - startIndex
        return maxLength



    def noRepeatingCharacters(self, s: str)->bool:
        counter = Counter()
        for c in s:
            counter[c] += 1
        for a in counter.values():
            if a >= 2:
                return False
        return True


# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
assert s.lengthOfLongestSubstring("bbbbb") == 1

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
assert s.lengthOfLongestSubstring("pwwkew") == 3

class Solution(object):
    def wordBreak(self, s, wordDict):
        self.s = s
        self.wordDict = wordDict
        return self.wordForPosition(0)

    def wordForPosition(self, pos):
        if len(self.s) == pos:
            return True
        editedString = self.s[pos:]
        for word in self.wordDict:
            if editedString[:len(word)] == word:
                if self.wordForPosition(pos + len(word)):
                    return True
        return False

s = Solution()
# assert s.wordBreak("leetcode", ["leet","code"])
print(s.wordBreak("cats", ["cat","s"]))
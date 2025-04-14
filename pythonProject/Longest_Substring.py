class CharacterHashMap:
    def __init__(self):
        self.list = [None] * 10
    def insert(self, character, value):
        if self.list[self.charHash(character)] is None:
            self.list[self.charHash(character)] = list()
        if not self.contains(character):
            self.list[self.charHash(character)].append((character, value))

    def contains(self, character):
        if self.list[self.charHash(character)] is None:
            return False
        for c,v in self.list[self.charHash(character)]:
            if character == c:
                return v
        return None

    @staticmethod
    def charHash(character):
        return ord(character) % 10

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.recordedCharacters = dict()
        length = 0
        max_length = 0
        for c in s:
            if not self.seenCharacter(c):
                self.recordedCharacters[c] = 0
                length += 1
            else:
                self.recordedCharacters = dict()
                length = 0
            if length > max_length:
                max_length = length
        return max_length

    def seenCharacter(self, character):
        return s in self.recordedCharacters

s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
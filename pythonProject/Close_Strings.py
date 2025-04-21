from collections import Counter
class Solution(object):

    def switch(self, word1, word2):
        sort1 = "".join(sorted(word1))
        sort2 = "".join(sorted(word2))
        return sort1 == sort2

    def closeStrings(self, word1, word2):
        count1 = Counter()
        count2 = Counter()
        for c1 in word1:
            count1[c1] += 1
        for c2 in word2:
            count2[c2] += 1
        return sorted(list(count1.values())) == sorted(list(count2.values()))



s = Solution()

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
assert s.switch("abc", "bca")

assert s.closeStrings("abb", "baa")

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
assert s.closeStrings("cabbba", "abbccc")
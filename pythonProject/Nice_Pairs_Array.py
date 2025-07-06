from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        revs = [self.rev(i) - i for i in nums]
        count = Counter()
        for rev in revs:
            count[rev] += 1
        pairs = [self.permutation(x) for x in count.values()]
        return sum(pairs)

    def nicePair(self, i: int, j: int) -> bool:
        return self.rev(i) + j == i + self.rev(j)

    def permutation(self, n: int) -> int:
        return n * (n - 1) // 2

    def rev(self, i: int) -> int:
        num = str(i)
        num = list(num)
        num = reversed(num)
        num = list(num)
        num = "".join(num)
        return int(num)

s = Solution()
# Example 1:
#
# Input: nums = [42,11,1,97]
# Output: 2
assert s.countNicePairs([42,11,1,97]) == 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# Example 2:
#
# Input: nums = [13,10,35,24,76]
assert s.countNicePairs([13,10,35,24,76]) == 4
# Output: 4
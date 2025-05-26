class Solution(object):
    def longestValidParentheses(self, s):
        maxLength = 0
        stack = list()
        exclusiveStart = -1
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        maxLength = max(maxLength, i - stack[-1])
                    else:
                        maxLength = max(maxLength, i - exclusiveStart)
                else:
                    exclusiveStart = i
        return maxLength

# Example 1:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# Output: 0

s = Solution()
assert s.longestValidParentheses("(()") == 2
assert s.longestValidParentheses(")()())") == 4
assert s.longestValidParentheses("((())") == 4
assert s.longestValidParentheses("") == 0


class Solution(object):
    def longestPalindrome(self, s):
        longest_palindrome = 0
        best_palindrome = ""
        for i in range(len(s)):
            this_palindrome_length = self.palindromeAtIndex(s,i)
            if this_palindrome_length > longest_palindrome:
                longest_palindrome = this_palindrome_length
                if this_palindrome_length % 2 == 1:
                    best_palindrome = s[i - this_palindrome_length//2 : i + 1 + this_palindrome_length//2]
                else:
                    best_palindrome = s[i - (this_palindrome_length - 1)//2: i + 2 + (this_palindrome_length - 1) // 2]
        return best_palindrome

    def slowLongestPalindrome(self,s):
        longest_palindrome = 1
        best_palindrome = s[0]
        for startIVX in range(len(s) - 1):
            for endIVX in range(1, len(s)):
                test_string = s[startIVX: endIVX]
                if len(test_string) > longest_palindrome:
                    if self.isPalindrome(test_string):
                        best_palindrome = test_string
                        longest_palindrome = len(test_string)

    def palindromeAtIndex(self,s,i):
        even_length = 0
        even_test = 0
        longest_even_palindrome = 0
        while (even_length != -1) and (i + even_test <= len(s)) and (i - even_test >= 0):
            even_length = self.palindromeLength(s[i-even_test: i + 2 + even_test])
            longest_even_palindrome = max(even_length, longest_even_palindrome)
            even_test += 1
        odd_length = 1
        odd_test = 1
        longest_odd_palindrome = 1
        while (odd_length != -1) and (i + odd_test <= len(s)) and (i - odd_test >= 0):
            odd_length = self.palindromeLength(s[i - odd_test: i + 1 + odd_test])
            longest_odd_palindrome = max(odd_length, longest_odd_palindrome)
            odd_test += 1
        return max(longest_odd_palindrome, longest_even_palindrome)


    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        elif len(s) == 2:
            return s[0] == s[1]
        else:
            if s[0] == s[-1]:
                return self.isPalindrome(s[1:-1])
            else:
                return False

    def palindromeLength(self, s):
        if not self.isPalindrome(s):
            return -1
        else:
            return len(s)



sol = Solution()
assert sol.longestPalindrome("babad") in ["bab", "aba"]
assert sol.longestPalindrome("cbbd") == "bb"
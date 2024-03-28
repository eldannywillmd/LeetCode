import re
class Solution:
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

solution = Solution()

text = "0P"
print(solution.isPalindrome(text))
from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        s = Counter(s)
        t = Counter(t)

        if s != t:
            return True
        else:
            return False


s = "anagram"
t = "nagaram"
solution = Solution()
solution.isAnagram(s, t)

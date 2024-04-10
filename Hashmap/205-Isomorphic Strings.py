class Solution:
    def isIsomorphic(self, s, t):
        translation = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in translation:
                if translation[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                translation[s[i]] = t[i]
        return True

s = "paper"
t = "title"
solution = Solution()
print(solution.isIsomorphic(s,t))
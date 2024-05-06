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
                if t[i] not in translation.values():
                    translation[s[i]] = t[i]
                else:
                    return False
        return True

s = "badc"
t = "baba"
solution = Solution()
print(solution.isIsomorphic(s,t))
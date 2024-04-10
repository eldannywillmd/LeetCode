class Solution:
    def wordPattern(self, pattern,s):
        s = s.split()
        translation = {}
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in translation:
                if translation[pattern[i]] != s[i]:
                    return False
                else:
                    continue
            else:
                if s[i] not in translation.values():
                    translation[pattern[i]] = s[i]
                else:
                    return False
        return True


pattern = "abba"
s = "dog dog dog dog"
solution = Solution()
print(solution.wordPattern(pattern, s))
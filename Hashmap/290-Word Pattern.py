class Solution:
    def wordPattern(self, pattern,s):
        s = s.split()
        translation = {}
        for i in range(len(pattern)):
            if pattern[i] in translation:
                if translation[pattern[i]] != s[i]:
                    return False
                else:
                    continue
            else:
                translation[pattern[i]] = s[i]
        return True


pattern = "aaaa"
s = "dog dog dog dog"
solution = Solution()
print(solution.wordPattern(pattern, s))
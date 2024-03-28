class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs[0])):
            prefix = strs[0][:len(strs[0])-i]
            for j in range(1, len(strs)):
                if strs[j][:len(prefix)] == prefix:
                    if j == len(strs) - 1:
                        return prefix
                    continue
                else:
                    break
        return ""

solution = Solution()
strs = ["flower","florwer","flozwer","flrower"]
print(solution.longestCommonPrefix(strs))
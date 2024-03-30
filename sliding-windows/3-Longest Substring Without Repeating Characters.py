class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        max_l = 0
        char_dict = {}
        index = 0
        for char in s:
            if char not in char_dict.keys():
                char_dict[char] = 1
                l += 1
            else:
                char_dict[char] += 1
                l += 1
                while char_dict[char] >= 2:
                    char_dict[s[index]] -= 1
                    index += 1
                    l -= 1
            if max_l < l:
                max_l = l
        return max_l

s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
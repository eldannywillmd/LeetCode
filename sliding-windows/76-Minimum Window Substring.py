from collections import Counter


class Solution:
    def minWindow(self, s,t):
        t_len = len(t)
        l = 0
        r = t_len - 1
        t_count = Counter(list(t))
        t_set = set(list(t))
        t_len = len(t)
        count = Counter()
        total_length = len(s)
        minWindow = ""

        if total_length >= t_len:
            #start count
            for i in range(t_len):
                if s[i] in t_set:
                    count[s[i]] += 1
            if count == t_count:
                minWindow = s[l:r+1]
                return minWindow

            # Check the loop statement
            while r < total_length - 1 and l <= r:
                while count != t_count and l <= r:
                    r += 1
                    if s[r] in t_set:
                        count[s[r]] += 1
                        while count[s[r]] > t_count[s[r]] and l < r:
                            if s[l] in t_set:
                                count[s[l]] -= 1
                            l += 1
                    if r == total_length - 1:
                        break
                while count == t_count and l <= r:
                    if count == t_count and (len(minWindow) > len(s[l:r+1]) or minWindow == ""):
                        minWindow = s[l:r+1]
                    if s[l] in t_set:
                        count[s[l]] -= 1
                    l += 1

            return minWindow
        else:
            return ""

s = "bba"
t = "ab"
solution = Solution()
print(solution.minWindow(s,t))
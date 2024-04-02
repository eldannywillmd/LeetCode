from collections import Counter

class Solution:
    def minWindow(self, s, t):
        min_sub = s
        t_count = Counter(t)
        count = Counter()
        sub = ""
        is_sub = False

        for char in s:
            sub += char
            if char in t_count:
                count[char] += 1
            while count[sub[0]] > t_count[sub[0]] or sub[0] not in t_count:
                if sub[0] in t_count and count[sub[0]] != t_count[sub[0]]:
                    count[sub[0]] -= 1
                    sub = sub[1:]
                elif len(sub) > 1 and sub[0] not in t_count:
                    sub = sub[1:]
                elif sub[0] in t_count and count[sub[0]] <= t_count[sub[0]] or len(sub) == 1:
                    break
            if is_sub == True:
                min_sub = min(min_sub, sub, key=len)[:]
            elif is_sub == False and count >= t_count:
                if is_sub == False:
                    is_sub = True
                min_sub = min(min_sub, sub, key=len)[:]

        if not is_sub:
            return ""
        else:
            return min_sub

s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s,t))
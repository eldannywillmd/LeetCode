from collections import Counter

class Solution:
    def minWindow(self, s, t):
        min_sub, sub = s, ""
        t_count, count = Counter(t), Counter()
        is_sub = False

        for char in s:
            sub += char
            if char in t_count:
                count[char] += 1
            while count[sub[0]] > t_count[sub[0]] or sub[0] not in t_count:
                if sub[0] in t_count and count[sub[0]] <= t_count[sub[0]] or len(sub) == 1:
                    break
                elif sub[0] in t_count and count[sub[0]] != t_count[sub[0]]:
                    count[sub[0]] -= 1
                    sub = sub[1:]
                elif sub[0] not in t_count:
                    sub = sub[1:]
            if is_sub == True:
                min_sub = min(min_sub, sub, key=len)[:]
            elif is_sub == False and len(sub) >= len(t) and count >= t_count:
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
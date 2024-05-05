from collections import Counter
class Solution:
    def minAnagramLength(self, s):
        count = Counter(s)
        minindex = len(s)
        for char in s:
            if count[char] % 2 == 0:
                minindex = min(minindex, count[char])
            elif count[char] == 1:
                return len(s)
            elif (all(value % count[char] == 0 for value in count.values())):
                return len(s)//count[char]
            else:
                return len(s)
        return len(s)//minindex
s = "abcdefgabcdefg"
# {a: 2, b: 2}
solution = Solution()
print(solution.minAnagramLength(s))
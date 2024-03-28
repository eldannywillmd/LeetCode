class Solution:
    def reverseWords(self, s):
        s = ' '.join(s.split()).split(" ")
        r = len(s) - 1
        l = 0
        while l <= r:
            swap = s[l]
            s[l] = s[r]
            s[r] = swap
            l += 1
            r -= 1

        return ' '.join(s)

    def reverseWords2(self, s):
        return " ".join(s.split()[::-1])

solution = Solution()
s = "the sky is    blue"
print(solution.reverseWords2(s))
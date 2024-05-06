class Solution:
    def isHappy(self, n):
        sqsum = 0
        n_map = {}
        while n != 0:
            sqsum += (n % 10) * (n % 10)
            n = n // 10
            if n == 0 and sqsum == 1:
                return True
            elif sqsum not in n_map.keys() and n == 0:
                n_map[sqsum] = 1
                n = sqsum
                sqsum = 0
            elif sqsum in n_map.keys() and n == 0:
                print(n_map)
                return False

n = 7
solution = Solution()
print(solution.isHappy(n))
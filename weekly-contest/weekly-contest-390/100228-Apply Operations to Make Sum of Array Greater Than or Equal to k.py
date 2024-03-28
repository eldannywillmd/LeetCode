import math


class Solution:
    import math
    def minOperations(self, k):
        num = [1]
        total = 1
        count = 0
        while total < k:
            if num[-1] < math.sqrt(k):
                num[-1] += 1
                count += 1
                total += 1
            else:
                num.append(num[-1])
                count += 1
                total += num[-1]
        return count

        # 100 = [10,10,10,...,10] 18 9 + 9
        # 81 = [9,9,9,9,9,9,9,9,9] 16 8 + 8
        # 20 -> [5,5,5,5] 4 + 3 [4,4,4,4,4]  3 + 4

solution = Solution()
print(solution.minOperations(20))
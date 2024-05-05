from collections import defaultdict


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word, k):
        count = defaultdict(int)
        max_count = 1

        for i in range(len(word)//k):
            count[word[k*i:k*(i+1)]] += 1
            max_count = max(count[word[k*i:k*(i+1)]], max_count)

        return len(word) // k - max_count

word = "leetcoleet"
k = 2
solution = Solution()
print(solution.minimumOperationsToMakeKPeriodic(word, k))

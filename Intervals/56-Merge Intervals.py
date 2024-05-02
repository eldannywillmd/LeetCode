class Solution:
    def merge(self, intervals):
        new_intervals = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if new_intervals:
                if new_intervals[-1][0] <= interval[0] <= new_intervals[-1][1] or new_intervals[-1][0] <= interval[1] <= new_intervals[-1][1]:
                    # overlap = True
                    new_intervals[-1][0] = min(new_intervals[-1][0], interval[0])
                    new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
                else:
                    # overlap = False
                    new_intervals.append(interval)
            else:
                new_intervals.append(interval)

        return new_intervals



intervals = [[1,2],[3,5],[2,4]]
# intervals = [[1,4],[0,0]]
solution = Solution()
print(solution.merge(intervals))
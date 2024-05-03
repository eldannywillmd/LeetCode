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
    def insert(self, intervals, newInterval):
        new_intervals = []

        if intervals:
            for interval in intervals:
                if newInterval:
                    if newInterval[0] <= interval[0] <= newInterval[1] or newInterval[0] <= interval[1] <= newInterval[1]:
                        # overlap = True -> merge
                        new_intervals.append([min(newInterval[0], interval[0]), max(newInterval[1], interval[1])])
                        newInterval = []
                    elif newInterval[0] <= interval[0]:
                        # overlap = False
                        new_intervals.append(newInterval)
                        new_intervals.append(interval)
                    else:
                        new_intervals.append(interval)
                else:
                    new_intervals.append(interval)

        else:
            new_intervals = [newInterval]
            return new_intervals

        if newInterval:
            new_intervals.append(newInterval)

        # make sure the intervals are merged
        new_intervals = self.merge(new_intervals)

        return new_intervals

intervals = [[1,5]]
newInterval = [2,3]
solution = Solution()
print(solution.insert(intervals, newInterval))
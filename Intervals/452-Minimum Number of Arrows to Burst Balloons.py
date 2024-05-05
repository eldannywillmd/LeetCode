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
    def findMinArrowShots(self, points):
        numArrows = len(points)
        overlaps = []
        while points:
            balloon = points.pop()
            for point in points:
                if point[0] <= balloon[0] <= point[1] or point[0] <= balloon[1] <= point[1]:
                    # add overlap to the list
                    overlaps.append([max(point[0], balloon[0]), min(point[1], balloon[1])])

        overlaps = self.merge(overlaps)
        numArrows -= len(overlaps)
        return numArrows

points = [[1,2],[2,3],[3,4],[4,5]]
solution = Solution()
print(solution.findMinArrowShots(points))
class Solution(object):
    def countIntersectingIntervals(self, intervals):
        n = len(intervals)
        intervals.sort()
        t, j = 0, 0
        for i in range(n):
                j = i + 1
                while j < n and intervals[i][1] >= intervals[j][0]:
                    j += 1
                t += j - i - 1
        return t
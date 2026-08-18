class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        n = len(intervals)
        intervals.sort(key = lambda i : i[1])
        lastEnd = intervals[0][1]
        count = 0
        for i in range(n):
            if intervals[i][0] >= lastEnd:
                count += 1
                lastEnd = intervals[i][1]
        return (n - count - 1)
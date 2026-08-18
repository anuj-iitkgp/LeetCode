class Solution(object):

  def insert(self, intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Part 1: Add all intervals that come before the newInterval (no overlap)
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Part 2: Merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged newInterval
    res.append(newInterval)

    # Part 3: Add all remaining intervals that come after newInterval (no overlap)
    while i < n:
        res.append(intervals[i])
        i += 1

    return res
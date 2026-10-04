class Solution(object):
    def earliestTime(self, tasks):
        mini = float('inf')
        for i in range(len(tasks)):
            mini = min(mini, tasks[i][0] + tasks[i][1])
        return mini
        
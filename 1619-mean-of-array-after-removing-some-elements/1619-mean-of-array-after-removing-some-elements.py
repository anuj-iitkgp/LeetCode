class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        k = int(len(arr) * 0.05)
        n = len(arr)
        s = sum(arr[k:n-k])
        return float(s) / len(arr[k:n-k])
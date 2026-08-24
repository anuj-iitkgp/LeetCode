class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        ans = float('inf')
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[ i + 1]:
                ans = min(ans, i)
        return ans
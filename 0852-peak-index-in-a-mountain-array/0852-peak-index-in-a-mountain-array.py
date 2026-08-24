class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        # ans = float('inf')
        # for i in range(1, n - 1):
        #     if arr[i - 1] < arr[i] and arr[i] > arr[ i + 1]:
        #         ans = min(ans, i)
        # return ans
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0:
                return mid + 1
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                r = mid - 1
            elif arr[mid] < arr[mid + 1]:
                l = mid + 1
            
            


    
        

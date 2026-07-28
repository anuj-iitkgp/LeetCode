class Solution(object):
    def findKthPositive(self, arr, k):
    #    current = 1
    #    i = 0

    #    while True:
    #     if i < len(arr) and arr[i] == current:
    #         i += 1
    #     else:
    #         k -= 1
    #         if k == 0:
    #             return current
    #     current += 1
        
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k
        
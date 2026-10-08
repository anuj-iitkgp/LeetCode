class Solution(object):
    def minimumSwaps(self, nums):
        t, n = 0, len(nums)
        i, j = 0, n - 1

        while i < j:
            if nums[i] != 0:
                i += 1
            elif nums[j] == 0:
                j -= 1
            else:
                t += 1
                i += 1
                j -= 1
                
        return t
            
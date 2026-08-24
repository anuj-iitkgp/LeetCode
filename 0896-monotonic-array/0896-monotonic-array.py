class Solution(object):
    def isMonotonic(self, nums):
        
        n = len(nums)
        count = 0
        count1 = 0
        for i in range(1, n ):
            if nums[i - 1] <= nums[i] and i - 1 <= i:
                count += 1
            if nums[i - 1] >= nums[i] and i - 1 <= i:
                count1 += 1

        if count == n - 1 or count1 == n - 1:
            return True
        return False
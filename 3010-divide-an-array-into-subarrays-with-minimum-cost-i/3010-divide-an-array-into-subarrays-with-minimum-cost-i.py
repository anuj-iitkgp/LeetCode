class Solution(object):
    def minimumCost(self, nums):
        ans = nums[0]
        min1, min2 = nums[1], nums[2]
        for i in range(3, len(nums)):
            if min2 >= nums[i] or min1 >= nums[i]:
                min1 = min(min1, min2)
                min2 = nums[i]
        ans += min1 + min2
        return ans
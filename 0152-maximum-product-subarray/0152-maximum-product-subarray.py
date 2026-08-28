class Solution(object):
    def maxProduct(self, nums):

        if not nums:
            return 0
        
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        n = len(nums)

        for i in range(1, n):
            num = nums[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(curr_max * num, num)
            curr_min = min(curr_min * num, num)

            ans = max(ans, curr_max)
        return ans
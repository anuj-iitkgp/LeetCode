class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        
        for i in range(n):
            nums[i] %= 2
        
        prefix_count = [0]*(n + 1)
        prefix_count[0] = 1
        oddSum = 0
        ans = 0

        for num in nums:
            oddSum += num
            if oddSum >= k:
                ans += prefix_count[oddSum - k]
            prefix_count[oddSum] += 1
        return ans
        
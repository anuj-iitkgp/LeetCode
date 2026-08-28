class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        sum1 = sum(nums[:k])
        max_sum  = sum1
        for i in range(n - k):
            sum1 += nums[k + i] - nums[i]
            max_sum = max(max_sum, sum1)
            print(max_sum)
        return float(max_sum) / k

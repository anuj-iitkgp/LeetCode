class Solution(object):
    def countKDifference(self, nums, k):
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if i < j and abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans
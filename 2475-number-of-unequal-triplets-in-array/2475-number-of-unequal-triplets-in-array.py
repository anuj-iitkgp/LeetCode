class Solution(object):
    def unequalTriplets(self, nums):
        n = len(nums)
        t = 0
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]:
                        t += 1
        return t
        
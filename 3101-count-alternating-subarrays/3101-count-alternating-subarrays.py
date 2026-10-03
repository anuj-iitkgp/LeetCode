class Solution(object):
    def countAlternatingSubarrays(self, nums):
        n = len(nums)
        t = 0
        i, j = 0, 0
        t = 0
        while j < n:
            while j < n - 1 and nums[j] != nums[j + 1]:
                j += 1
            x = j - i + 1
            t += x * (x + 1) // 2
            j += 1
            i = j
        return t

            
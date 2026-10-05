class Solution(object):
    def duplicateNumbersXOR(self, nums):
        count = collections.Counter(nums)
        ans = 0
        for val, freq in count.items():
            if freq == 2:
                ans ^= val
        return ans
        
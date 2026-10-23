class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set([int(c) for c in s if c.isdigit()])
        nums = [c for c in nums]
        nums.sort()
        if len(nums) <= 1:
            return -1
        return nums[-2]
        
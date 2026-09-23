from collections import Counter
class Solution(object):
    def firstUniqueEven(self, nums):
        n = len(nums)
        count = Counter(nums)
        for num in nums:
            if num % 2 == 0 and count[num] == 1:
                return num
        return -1
        
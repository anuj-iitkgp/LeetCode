from collections import Counter
class Solution(object):
    def isPossibleToSplit(self, nums):
        count = Counter(nums)
        for freq in count.values():
            if freq > 2:
                return False
        return True
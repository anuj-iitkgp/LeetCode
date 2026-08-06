from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        counter = Counter(nums)

        return [num for num, count in counter.items() if count > n // 3]
        

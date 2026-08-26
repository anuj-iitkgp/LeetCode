from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        count = Counter(nums)
        print(count)
        sum1 = 0
        for val, freq in count.items():
            if freq == 1:
                sum1 += val
        return sum1


        
        
        
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)

 # approach 1 (Time and Space: O(n))       
        # counter = Counter(nums)

        # return [num for num, count in counter.items() if count > n // 3]

        if not nums:
            return []

        # Pass 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Pass 2: Verify candidates
        result = []
        n = len(nums)
        for cand in (candidate1, candidate2):
            if cand is not None and nums.count(cand) > n // 3:
                result.append(cand)

        return result
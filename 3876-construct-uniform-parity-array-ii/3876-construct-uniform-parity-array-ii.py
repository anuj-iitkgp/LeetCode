class Solution(object):
    def uniformArray(self, nums1):
        n = len(nums1)
        evens = [x for x in nums1 if x % 2 == 0]
        odds = [x for x in nums1 if x % 2 != 0]

        if not odds:
            return True
        min_odd = min(odds)

        for x in evens:
            if x < min_odd:
                return False
        return True
        
        
        
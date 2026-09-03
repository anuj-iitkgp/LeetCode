class Solution(object):
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 != 0:
                if x < min_odd:
                    min_odd = x
            else:
                if x < min_even:
                    min_even = x


        if min_odd == float('inf'):
            return True


        return min_even > min_odd
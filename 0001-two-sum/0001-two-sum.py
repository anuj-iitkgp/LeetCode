class Solution(object):

    def twoSum(self, nums, target):
        mp = {}
        for i, num in enumerate(nums):
            diff = - num + target
            if diff in mp:
                return [mp[diff], i]
            mp[num] = i
        return []


class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(num)
        ans += [x for x in nums if x % 2 == 1]
        return ans


        
class Solution(object):
    def sortColors(self, nums):
        count = [0] * 3

        for num in nums:
            count[num] += 1
        idx = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[idx] = i
                idx += 1

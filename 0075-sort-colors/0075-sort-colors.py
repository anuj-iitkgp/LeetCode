class Solution(object):
    def sortColors(self, nums):
       zero, one, two = 0, 0, 0
       n = len(nums)

       for i in range(n):
        if nums[i] == 0:
            nums[two] = 2
            nums[one] = 1
            nums[zero] = 0
            two += 1
            one += 1
            zero += 1
        elif nums[i] == 1:
            nums[two ] = 2
            nums[one] = 1
            two += 1
            one += 1
        else:
            nums[two] = 2
            two += 1

# time O(n), Space O(1)

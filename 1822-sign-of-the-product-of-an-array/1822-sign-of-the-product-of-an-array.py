class Solution(object):
    def arraySign(self, nums):
        
        # product = 1
        # n = len(nums)

        # for i in range(n):
        #     product *= nums[i]
        
        # if product > 0:
        #     return 1
        # elif product < 0:
        #     return -1
        # return 0
        

        n = len(nums)
        cnt = 0

        for i in range(n):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                cnt += 1
        
        if cnt % 2 == 1:
            return -1
        return 1
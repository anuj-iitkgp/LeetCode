class Solution(object):
    def rearrangeArray(self, nums):
        # even = 0
        # odd = 1

        # while even < len(nums) and odd < len(nums) :
        #     if nums[odd] > 0 and nums[even] < 0:
        #         nums[odd], nums[even] = nums[even], nums[odd]
        #         odd += 1
        #         even += 2
        #     else:
        #         even += 2
   
        # return nums

        pos = []
        neg = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        i, j = 0, 0
        res = []
        while i < len(pos) and j < len(neg):
            res.append(pos[i])
            i += 1
            res.append(neg[j])
           
            j += 1
            
            
        return res


            
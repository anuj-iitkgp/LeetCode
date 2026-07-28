class Solution(object):
    def rearrangeArray(self, nums):
        even = 0
        odd = 1
        res = [0] * len(nums)

        for num in nums :
            if num > 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2
   
        return res

        # pos = []
        # neg = []

        # for num in nums:
        #     if num < 0:
        #         neg.append(num)
        #     else:
        #         pos.append(num)
        
        # i, j = 0, 0
        # res = []
        # while i < len(pos) and j < len(neg):
        #     res.append(pos[i])
        #     i += 1
        #     res.append(neg[j])
           
        #     j += 1
            
            
        # return res


            
class Solution(object):
    def canBeIncreasing(self, nums):
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1
                if count > 1:
                    return False
                
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                    
        return True












# class Solution(object):
#     def canBeIncreasing(self, nums):
#         n = len(nums)
#         for i in range(n):
#             new_nums = nums[:i] + nums[i+1:]
#             isInc = True
#             for j in range(1, len(new_nums)):
#                 if new_nums[j - 1] >= new_nums[j]:
#                     isInc = False
#                     break
#             if isInc:
#                 return True
#         return False
        
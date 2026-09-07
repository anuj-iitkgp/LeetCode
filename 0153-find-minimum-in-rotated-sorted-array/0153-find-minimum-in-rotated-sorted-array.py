class Solution(object):
    def findMin(self, nums):
        # return min(nums) # T.C. = O(n)

        # low, high = 0, len(nums) - 1
        # while low < high:
        #     mid = low + (high - low ) // 2

        #     if nums[mid] > nums[high]:
        #         low = mid + 1
        #     else:
        #         high = mid
        # return nums[low]
        l, r = 0, len(nums) - 1
        if l == r:
            return nums[l]
        

        while l < r:
            mid = (l + r) // 2

            if r - l <= 1:
                if nums[l] < nums[r]:
                    return nums[l]
                return nums[r]

            if nums[l] < nums[r]:
                return nums[l]
            if nums[mid - 1] > nums[mid]  and nums[mid] < nums[mid + 1]:
                return nums[mid]

            elif nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid - 1
        return nums[l]
            




        
        



        
class Solution(object):
    

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        ans = []

        def bst(nums, target):
            m = len(nums)
            low = 0
            high = m - 1

            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
   
        
        for i in range(n):
            ans.append(bst(matrix[i], target))
            if ans[i] == True:
                return True
                break
        return False
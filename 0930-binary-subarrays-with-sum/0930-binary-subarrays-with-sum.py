class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        res, currSum = 0, 0
        prefixSums = {0:1}

        for num in nums:
            currSum += num
            diff = currSum - goal

            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)

        return res


#brute force; Time:O(n^2) and constant space
        
        
        
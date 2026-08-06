class Solution(object):
    def subsetsWithDup(self, nums):
        # MUST sort first so all duplicate numbers are adjacent
        nums.sort()
        
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Pick
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            # Don't pick: Skip all duplicate elements following index i
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)
        return res
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def backtrack(start, sol):
            # 1. Every state in the recursion tree is a valid subset
            res.append(sol[:])

            # 2. Try including each remaining element starting from 'start'
            for i in range(start, len(nums)):
                # Skip duplicate elements at the same depth level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Include nums[i], recurse, and backtrack
                sol.append(nums[i])
                backtrack(i + 1, sol)
                sol.pop()

        backtrack(0, [])
        return res
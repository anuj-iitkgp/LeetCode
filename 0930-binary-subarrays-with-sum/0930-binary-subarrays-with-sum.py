class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def SubarraysLessThanGoal(nums, goal):
            n = len(nums)
            
            l, r = 0, 0
            sum1, count = 0, 0

            while r < n:
                if goal < 0:
                    return 0
                sum1 += nums[r]
                while sum1 > goal:
                    sum1 -= nums[l]
                    l += 1
                count += r - l + 1
                r += 1
            return count

        p = SubarraysLessThanGoal(nums, goal) 
        q = SubarraysLessThanGoal(nums, goal - 1)
        return (p - q)

# Time Com: O(1), Space: O(1)
        
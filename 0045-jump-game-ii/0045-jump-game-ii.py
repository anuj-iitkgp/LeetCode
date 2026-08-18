class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        minJump, maxJump = 0, 0
        currEnd = 0

        for i in range(n - 1):
            maxJump = max(maxJump, i + nums[i])

            if i == currEnd:
                minJump += 1
                currEnd = maxJump

                if currEnd >= n - 1:
                    break
        return minJump

        
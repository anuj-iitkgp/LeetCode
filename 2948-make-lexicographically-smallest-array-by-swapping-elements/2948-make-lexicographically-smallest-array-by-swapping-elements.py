from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        sted = sorted(nums)

        gn = 0
        sgnum = {}
        ele = {}

        prev = sted[0]

        for x in sted:
            if x - prev <= limit:
                sgnum[x] = gn
                ele.setdefault(gn, deque()).append(x)
            else:
                gn += 1
                sgnum[x] = gn
                ele.setdefault(gn, deque()).append(x)

            prev = x

        for i in range(len(nums)):
            group = sgnum[nums[i]]
            nums[i] = ele[group].popleft()

        return nums
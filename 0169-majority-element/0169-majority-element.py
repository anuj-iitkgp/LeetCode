class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # count = 1
        # n = len(nums)
        # if n <= 1:
        #     return nums[0]

        # nums.sort()
        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         count += 1
        #         if count > math.floor(n // 2):
        #             return nums[i]
        
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


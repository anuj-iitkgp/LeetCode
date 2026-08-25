class Solution(object):
    def thirdMax(self, nums):
        n = len(nums)
        first, second = None, None
        third = None

        for i in range(n):
            
            if nums[i] in (first, second, third):
                continue


            if first is None or nums[i] > first:
                third = second
                second = first
                first = nums[i]

            elif second is None or nums[i] > second:
                third = second
                second = nums[i]

            elif third is None or nums[i] > third:
                third = nums[i]
                

        return third if third is not None else first
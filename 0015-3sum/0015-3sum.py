class Solution(object):

    def threeSum(self, nums):
        n = len(nums)

        nums.sort()
        res = []

        for i in range(n - 2):
            # If the current number is > 0, no remaining 3 numbers can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate first element (compare with PREVIOUS element)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate left and right elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1



        return res
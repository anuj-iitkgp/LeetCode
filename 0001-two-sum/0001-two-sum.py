class Solution(object):

    def twoSum(self, nums, target):
        n = len(nums)

        # Store value along with its original index: [(val, original_index), ...]
        indexed_nums = [(nums[i], i) for i in range(n)]
        indexed_nums.sort()

        left = 0
        right = n - 1

        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return [indexed_nums[left][1], indexed_nums[right][1]]

        return []
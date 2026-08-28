class Solution(object):
    def longestConsecutive(self, nums):
        # n = len(nums)
        # if not nums:
        #     return 0
        # nums.sort()
        # max_streak = 1
        # current_streak = 1

        # for i in range(n - 1):
        #     if nums[i + 1] == nums[i]:
        #         continue
        #     if nums[i + 1] - nums[ i ] == 1:
        #         current_streak += 1
        #     else:
        #         max_streak = max(max_streak, current_streak)
        #         current_streak = 1
        # return max(max_streak, current_streak)

        num_set = set(nums)  # O(n) space and time build
        longest_streak = 0

        for num in num_set:
        # Only start counting if 'num' is the beginning of a sequence

            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

            # Count consecutive numbers

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def helper(nums, k):
            mp = {}
            total = 0

            left, right = 0, 0
            n = len(nums)

            while right < n:
                if nums[right] in mp:
                    mp[nums[right]] += 1
                else:
                    mp[nums[right]] = 1

                while len(mp) > k:
                    mp[nums[left]] -= 1
                    if mp[nums[left]] == 0:
                        del mp[nums[left]]
                    left += 1
                total += right - left + 1
                right += 1
            return total
        return helper(nums, k) - helper(nums, k - 1)
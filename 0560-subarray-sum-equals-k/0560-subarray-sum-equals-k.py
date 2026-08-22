# class Solution(object):

#   def subarraySum(self, nums, k):
#     n = len(nums)
#     count = 0

#     for l in range(n):
#       sum1 = 0
#       for r in range(l, n):
#         sum1 += nums[r]
#         if sum1 == k:
#           count += 1

#     return count

class Solution(object):

  def subarraySum(self, nums, k):
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}

    for num in nums:
      current_sum += num

      # If (current_sum - k) exists in map, it means there is a valid subarray
      if (current_sum - k) in prefix_counts:
        count += prefix_counts[current_sum - k]

      # Update the frequency of current_sum
      prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count





from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        
        # Sort the (num, count) pairs by count in descending order
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        output = []
        for num, count in sorted_counts:
            output.append(num)
            if len(output) == k:
                return output
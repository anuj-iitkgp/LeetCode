from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        # counts = Counter(nums)
        
        # # Sort the (num, count) pairs by count in descending order
        # sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # output = []
        # for num, count in sorted_counts:
        #     output.append(num)
        #     if len(output) == k:
        #         return output
        # T.C. O(nlogk) and Space: O(n)

# another approach

        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]



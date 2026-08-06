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
        # T.C. O(nlogn) and Space: O(n)

# another approach

        # counter = Counter(nums)
        # heap = []

        # for key, val in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (val, key))
        #     else:
        #         heapq.heappushpop(heap, (val, key))
        
        # return [h[1] for h in heap]

        # T.C. O(nlogk) and Space: O(n)

# optimize approach

        n = len(nums)

        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ans = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ans.extend(buckets[i])
            if len(ans) == k:
                break
        return ans


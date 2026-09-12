import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        # Store original indices along with [l, r, weight]
        ext_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            ext_intervals.append((l, r, w, i))
        
        # Sort intervals by their right boundary (end time)
        ext_intervals.sort(key=lambda x: x[1])
        
        # Precompute the latest non-overlapping interval for each interval using binary search
        ends = [x[1] for x in ext_intervals]
        prev = []
        for i in range(n):
            l = ext_intervals[i][0]
            # Find the largest index j such that ext_intervals[j][1] < l
            idx = bisect.bisect_left(ends, l) - 1
            prev.append(idx)
            
        # dp[c][i] = (max_weight, list_of_indices)
        # c ranges from 0 to 4 (number of intervals picked)
        # i ranges from -1 to n - 1 (representing prefix of intervals)
        
        # Base case: 0 intervals picked gives weight 0 and empty index list
        memo = {}
        
        def solve():
            # We can use a bottom-up DP table or memoized recursion.
            # Given constraints (n up to 50,000), a bottom-up array approach or optimized DP is best.
            pass

        # Optimized bottom-up DP arrays for speed and memory:
        # dp[c][i] stores the max weight choosing c intervals from the first i+1 intervals
        # To reconstruct the lexicographically smallest indices, we can store the best choices or trace back.
        
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for c in range(1, 5):
            for i in range(1, n + 1):
                # Option 1: Do not include the current interval (i-1)
                best_weight, best_indices = dp[c][i - 1]
                
                # Option 2: Include the current interval (i-1)
                cur_l, cur_r, cur_w, cur_idx = ext_intervals[i - 1]
                p = prev[i - 1] # index in ext_intervals (0-indexed, so corresponds to p+1 in 1-based dp)
                
                prev_weight, prev_indices = dp[c - 1][p + 1]
                inc_weight = cur_w + prev_weight
                
                # Compare weights, and for lexicographical tie-breaking, compare index lists
                inc_indices = sorted(prev_indices + [cur_idx])
                
                if inc_weight > best_weight:
                    dp[c][i] = (inc_weight, inc_indices)
                elif inc_weight == best_weight:
                    if not best_indices or inc_indices < best_indices:
                        dp[c][i] = (inc_weight, inc_indices)
                    else:
                        dp[c][i] = (best_weight, best_indices)
                else:
                    dp[c][i] = (best_weight, best_indices)
                    
        # Find the best result among c = 0 to 4
        max_w = -1
        best_ans = []
        for c in range(5):
            w, idxs = dp[c][n]
            if w > max_w:
                max_w = w
                best_ans = idxs
            elif w == max_w:
                if not best_ans or idxs < best_ans:
                    best_ans = idxs
                    
        return best_ans
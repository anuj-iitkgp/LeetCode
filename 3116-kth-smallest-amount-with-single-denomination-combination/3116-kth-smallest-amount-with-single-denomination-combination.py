class Solution:
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(coins)
        
        subsets = []
        for mask in range(1, 1 << n):
            l = 1
            bits = 0
            for i in range(n):
                if mask & (1 << i):
                    l = l * coins[i] // gcd(l, coins[i])
                    bits += 1
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((l, sign))
        
        def count_le(x):
            total = 0
            for l, sign in subsets:
                total += sign * (x // l)
            return total
        
        min_coin = min(coins)
        lo, hi = 1, min_coin * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
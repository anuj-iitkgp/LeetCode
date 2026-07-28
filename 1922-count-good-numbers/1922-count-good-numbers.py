class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        # Calculate (5^even_positions * 4^odd_positions) % MOD
        ans = (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD
        
        return ans
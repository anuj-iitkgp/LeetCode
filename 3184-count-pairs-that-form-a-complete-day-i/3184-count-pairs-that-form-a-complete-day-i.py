class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n, t = len(hours), 0
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    t += 1
        return t
        
class Solution(object):
    def maximumWealth(self, accounts):
        n = len(accounts)
        maxW = float('-inf')
        for i in range(n):
            maxW = max(maxW, sum(accounts[i]))
        return maxW
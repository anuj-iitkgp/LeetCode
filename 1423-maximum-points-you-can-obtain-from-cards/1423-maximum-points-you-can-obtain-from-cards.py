class Solution(object):
    def maxScore(self, cardPoints, k):
        
        curr_sum = sum(cardPoints[:k]) # sum of first k element from the left
        max_sum = curr_sum

        n = len(cardPoints)
        #swao left cards for right cards one by one

        for i in range(1, k + 1):
            curr_sum = curr_sum - cardPoints[k - i] + cardPoints[n - i] # remove left, add right
            max_sum = max(curr_sum, max_sum)
        return max_sum




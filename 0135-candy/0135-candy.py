class Solution(object):
    def candy(self, ratings):
        """
        Approach: Two-Pass Greedy ($O(n)$ Time, $O(n)$ Space)To ensure every child gets at least 1 candy and children with higher ratings than their neighbors get more candies:
        1. Initialize: Give every child 1 candy initially.

        
        2. Left-to-Right Pass: Iterate from left to right (1 to n-1). If ratings[i] > ratings[i - 1], set candies[i] = candies[i - 1] + 1. This satisfies the condition for left neighbors.
        
       3. Right-to-Left Pass: Iterate from right to left (n-2 down to 0). If ratings[i] > ratings[i + 1], update candies[i] = max(candies[i], candies[i + 1] + 1). Using max ensures we don't break the condition established in the left pass.
       
       4. Result: Return the sum of all elements in the candies array.
        """
        n = len(ratings)
        candies = [1] * n
        
        # Left-to-Right 
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candies[i] = 1 + candies[i - 1]
        
        # Right-to-Left
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i], 1 + candies[i + 1])
        
        return sum(candies)


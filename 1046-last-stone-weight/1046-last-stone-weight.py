class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:

            first_idx = stones.index(max(stones))
            first = stones.pop(first_idx)  
            

            second_idx = stones.index(max(stones))
            second = stones.pop(second_idx)  
            

            if first != second:
                stones.append(first - second)
                
        return stones[0] if stones else 0
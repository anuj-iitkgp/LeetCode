class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        
        jewel_set = set(jewels)
        cnt = sum(1 for stone in stones if stone in jewel_set)
        return cnt
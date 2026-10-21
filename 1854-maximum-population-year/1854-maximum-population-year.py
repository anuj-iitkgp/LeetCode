class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        # Create an array for the 101 possible years (1950 to 2050)
        pop_changes = [0] * 101
        
        # Mark the start of a life (+1) and the end of a life (-1)
        for birth, death in logs:
            pop_changes[birth - 1950] += 1
            pop_changes[death - 1950] -= 1
            
        max_pop = 0
        current_pop = 0
        earliest_year = 1950
        
        # Calculate the prefix sum to find the actual population per year
        for i in range(101):
            current_pop += pop_changes[i]
            
            # Update if we find a strictly greater population
            if current_pop > max_pop:
                max_pop = current_pop
                earliest_year = 1950 + i
                
        return earliest_year
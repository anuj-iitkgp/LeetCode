class Solution(object):
    def minOperations(self, nums, x):
        m = len(nums)
        
        # Array duplicate karke prefix + suffix loop handling seamless banayi
        duplicated_nums = nums + nums
        n = len(duplicated_nums)
        
        current_sum = 0
        i = 0
        j = 0
        ans = float('inf')
        flag = False

        while j < n:
            current_sum += duplicated_nums[j]
            j += 1

            # Sum x se bada hone par left side se shrink karein
            while current_sum > x and i < j:
                current_sum -= duplicated_nums[i]
                i += 1

            if current_sum == x:
                valid = False
                # Pure prefix (original array ke andar)
                if i == 0 and j <= m:
                    valid = True
                # Pure suffix (original array ke andar)
                elif j == m and i >= 0:
                    valid = True
                # Suffix + Prefix boundary cross kar raha ho
                elif i < m and j > m:
                    valid = True

                if valid:
                    ans = min(ans, j - i)
                    flag = True

        return ans if (flag and ans <= m) else -1
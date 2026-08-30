class Solution(object):
    def numberOfSubstrings(self, s):
       #----------- Brute force --------- 
        # n = len(s)
        # count = 0

        # for i in range(n):
        #     hash_set = set()
        #     for j in range(i, n):
        #         hash_set.add(s[j])
        #         if len(hash_set) == 3:
        #             count += (n - j)
        #             break
        # return count

        #-------- Optimal -------

        n = len(s)
        count = 0
        last_seen = [-1, -1, -1]

        for i in range(n):
            last_seen[ord(s[i]) - ord('a')] = i

            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                count += 1 + min(last_seen)
        
        return count
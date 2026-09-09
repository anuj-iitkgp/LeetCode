class Solution(object):
    def reverseDegree(self, s):
        n = len(s)
        ans = 0
        reversed_dict = {char: 26 - i for i, char in enumerate(string.ascii_lowercase)}

        for i in range(1, n + 1):
            ans += i * reversed_dict[s[i - 1]]
        return ans


            

        
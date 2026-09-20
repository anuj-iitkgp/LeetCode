class Solution(object):
    def reverseDegree(self, s):
        return sum(i * (123 - ord(char)) for i, char in enumerate(s, start=1))


       
            

        
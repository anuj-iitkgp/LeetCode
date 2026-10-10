class Solution(object):
    def countMonobit(self, n):
        t = 0
        for i in range(n + 1):
            b = bin(i)[2:]
            s = 0
            for i in range(len(b) - 1):
                if b[i] != b[i+1]:
                    break
                s += 1
            if s == len(b) - 1:
                t += 1
        return t

        
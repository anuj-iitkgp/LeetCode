class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))
        flag = 1
        ans = ""  
        store = ""
        for i in range(len(s)):
            if s[i] != "9" and flag:
                store = s[i]
                s[i] = "9"
                flag = 0
            if s[i] == store:
                s[i] = "9"
        maxi = int("".join(s))
        print(maxi)
        
        s1 = list(str(num))
        f = 1
        store1 = ""
        for i in range(len(s1)):
            if f:

                if i == 0 and s1[i] != "1":
                    store1 = s1[i]
                    ans = "1"
                    s1[i] = ans
                    f = 0

                elif i > 0 and s1[i] not in ["0", "1"]:
                    store1 = s1[i]
                    ans = "0"
                    s1[i] = ans
                    f = 0
            elif s1[i] == store1:
                s1[i] = ans
           
        mini = int("".join(s1))
        print(mini)

        return maxi - mini
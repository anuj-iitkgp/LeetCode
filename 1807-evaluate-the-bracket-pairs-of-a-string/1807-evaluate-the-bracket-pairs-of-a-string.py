class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        store = {}
        i = 0
        j = 0
        n = len(s)
        ans=""
        for i in range(len(knowledge)):
            store[knowledge[i][0]] = knowledge[i][1]
        i=0
        while(j<n):
            if s[i]=='(':
                j=i+1
                while s[j]!=')':
                    j+=1
                chk = s[i+1:j]
                print(chk)
                val = store.get(chk,"?")
                ans+=val
                i=j+1
                j=j+1
            else:
                ans+=s[i]
                i+=1
                j+=1
        return ans
            
        
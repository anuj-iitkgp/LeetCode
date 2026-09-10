class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)
        ans = []
        for i in range(n):
            ans.append([heights[i], names[i]])
        ans.sort(reverse = True)

        for i in range(n):
            names[i] = ans[i][1]
        return names
        

        
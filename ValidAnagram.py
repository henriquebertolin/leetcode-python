class Solution(object):
    def isAnagram(self, s, t):
        sList = list(s)
        tList = list(t)
        tList.sort()
        sList.sort()
        return (sList == tList)
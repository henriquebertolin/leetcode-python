class Solution(object):
    def lengthOfLastWord(self, s):
        l = 0
        r = len(s)-1
        cont = 0
        while l <= r:
            if s[r] == " ":
                r-=1
                cont = 0
            if s[l] == " ":
                l+=1
                cont = 0
            if s[l].isalpha() and s[r].isalpha():
                cont += 1
                l+=1
        return(cont)
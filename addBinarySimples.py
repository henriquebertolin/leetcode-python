class Solution(object):
    def addBinary(self, a, b):

        a = int(a,2)
        b = int(b,2)
        a = a+b
        a = bin(a)
        return a[2:]
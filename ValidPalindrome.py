class Solution(object):
    def isPalindrome(self, s):
        newString = ''
        for char in s:
            if char.isalnum():
                newString += char
        newStringReverse = newString[::-1]
        newStringReverse = newStringReverse.upper()
        newString = newString.upper()
        return newString == newStringReverse
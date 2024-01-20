class Solution(object):
    def plusOne(self, digits):
        string = ''
        for i in range(len(digits)):
            string += string.join(str(digits[i]))
        string = int(string) + 1
        string = str(string)
        digits2 = list(string)
        for i in range(len(digits2)):
            digits2[i] = int(digits2[i])
        return (digits2)
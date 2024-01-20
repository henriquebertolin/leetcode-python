class Solution(object):
    def addBinary(self, a, b):
        if a == '0' and b == a:
            return '0'
        maior = a
        if len(b) > len(a):
            maior = b

        menor = b
        if len(b) > len(a):
            menor = a
        res = ''
        carry = False
        #if len(maior) != len(menor):
        # maior = maior[::-1]
        # menor = menor[::-1]
        for i in range(len(menor)-1, -1, -1):
            if (not carry):
                if menor[i] == '1' and maior[i+(len(maior)-len(menor))] == '1':
                    res += '0'
                    carry = True
                elif menor[i] != maior[i+(len(maior)-len(menor))]:
                    res += '1'
                    carry = False
                elif menor[i] == '0' and maior[i+(len(maior)-len(menor))] == '0':
                    res += '0'
                    carry = False
            else:
                if menor[i] == '1' and menor[i] == maior[i+(len(maior)-len(menor))]:
                    res += '1'
                    carry = True
                elif menor[i] != maior[i+(len(maior)-len(menor))]:
                    res += '0'
                    carry = True
                elif menor[i] == '0' and maior[i+(len(maior)-len(menor))] == '0':
                    res += '1' 
                    carry = False
        maior = maior[::-1]
        for i in range(len(menor), len(maior)):
            if carry:
                if maior[i] == '1':
                    res+= '0'
                    carry = True
                elif maior[i] == '0':
                    res += '1'
                    carry = False
            else:
                res += maior[i]
        if carry:
            res += '1'
        resReverse = res[::-1]
        return(resReverse)
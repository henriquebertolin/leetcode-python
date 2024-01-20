class Solution(object):
    def generate(self, numRows):
        pascal = []
        if numRows == 1:
            pascal.append([1])
            return (pascal)
        elif numRows == 2:
            pascal.append([1])
            pascal.append([1,1])
            return(pascal)
        else:
            pascal = [[1], [1,1]]
            for i in range (2, numRows):
                teste = [1] * (i+1)
                for j in range(len(pascal[i-1])-1):
                    teste[j+1] = pascal[i-1][j] + pascal[i-1][j+1]
                pascal.append(teste)
            return (pascal)
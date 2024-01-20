class Solution(object):
    def searchMatrix(self, matrix, target):
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if matrix[j][i] == target:
                    return(True)
        return (False)
    

    # class Solution(object):
    # def searchMatrix(self, matrix, target):
    #     cont = 0
    #     left, right = 0, len(matrix[cont])-1
    #     while True:
    #         if matrix[cont][left] > target:
    #             return (False)
    #             break
    #         elif matrix[cont][right] < target and cont < len(matrix)-1:
    #             cont+=1
    #         elif matrix[cont][left] <= target and matrix[cont][right] >= target:
    #             if matrix[cont][left] == target:
    #                 return (True)
    #                 break
    #             if matrix[cont][left] < target:
    #                 left+=1
    #             if matrix[cont][right] == target:
    #                 return (True)
    #                 break
    #             if matrix[cont][right] > target:
    #                 right -= 1
    #         else:
    #             return (False)
    #             break
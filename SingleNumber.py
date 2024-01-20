class Solution(object):
    def singleNumber(self, nums):
        numeros = {}
        for i in range(len(nums)):
            numeros[nums[i]]  = 1 + numeros.get(nums[i],0)
        print(numeros)
       # for i in range(len(nums)):
           # if nums[i] == 1:
                #return nums[i]
        for num in nums:
            if numeros[num] == 1:
                return (num)
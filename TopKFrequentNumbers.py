class Solution(object):
    def topKFrequent(self, nums, k):
        numeros = {}
        maiores = []
        for i in range(len(nums)):
            numeros[nums[i]] = 1 + numeros.get(nums[i], 0)
        numerosSorted = dict(sorted(numeros.items(), key=lambda item: item[1], reverse=True)[:k])
        for k in numerosSorted:
            maiores.append(k)
        return (maiores)
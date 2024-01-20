class Solution(object):
    def findDuplicate(self, nums):
        from collections import defaultdict

        #nums  = [1,3,4,2,2]
        numsDic = defaultdict(int)

        for i in range(len(nums)):
            if numsDic[nums[i]] == 0:
                numsDic[nums[i]] = 1 + numsDic.get(nums[i], 0)
            else:
                return (nums[i])
class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        if len(nums) > 0:
            r = 1
        else:
            r = 0
        aux = 0

        while r <= len(nums)-1:
            if nums[l] == 0:
                if nums[r] != 0:
                    aux = nums[r] 
                    nums[r] = nums[l]
                    nums[l] = aux
                    l += 1
                    r += 1
                elif nums[r] == 0:
                    r += 1
            else:
                r += 1
                l += 1
        return (nums)
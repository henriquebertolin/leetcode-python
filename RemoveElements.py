class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 1 and nums[0] != val:
            l = 1
            return l
        l, r = 0, len(nums)-1
        aux = 0
        while l <= r:
            if nums[l] == val:
                if nums[r] != val:
                    aux = nums[r]
                    nums[r] = nums[l]
                    nums[l] = aux
                    r-=1
                    l+=1
                else:
                    r-=1
            if nums[l] != val:
                l += 1
        return(l)
class Solution(object):
    def searchInsert(self, nums, target):
        r = len(nums) - 1
        l = 0

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
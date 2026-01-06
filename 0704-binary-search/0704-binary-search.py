class Solution(object):
    def search(self, nums, target):
        first=0
        last=len(nums)-1
        while first<=last:
            mid=first+(last-first)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                first=mid+1
            else:
                last=mid-1
        return -1
        
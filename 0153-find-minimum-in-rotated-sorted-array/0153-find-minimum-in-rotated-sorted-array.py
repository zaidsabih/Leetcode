class Solution(object):
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]
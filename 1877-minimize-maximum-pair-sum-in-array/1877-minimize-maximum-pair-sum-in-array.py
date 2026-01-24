class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        first=0
        last=len(nums)-1
        maximum=0
        while first<last:
            pair=nums[first]+nums[last]
            maximum=max(maximum,pair)
            first+=1
            last-=1
        return maximum
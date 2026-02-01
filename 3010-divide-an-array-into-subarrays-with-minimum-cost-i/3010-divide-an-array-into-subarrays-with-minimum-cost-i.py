# Added using AI
class Solution:
    def minimumCost(self, nums):
        first=nums[0]
        second=1000
        third=1000
        for i in range(1,len(nums)):
            if nums[i]<second:
                third=second
                second=nums[i]
            elif nums[i]<third:
                third=nums[i]
        return first+second+third
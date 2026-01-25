class Solution(object):
    def sortArrayByParityII(self, nums):
        i=0
        j=1
        while i<len(nums) and j<len(nums):
            if nums[i]%2==0:
                i+=2
            elif nums[j]%2==1:
                j+=2
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=2
                j+=2
        return nums
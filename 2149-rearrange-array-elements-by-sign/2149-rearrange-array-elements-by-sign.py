class Solution(object):
    def rearrangeArray(self, nums):
        answer=[0]*len(nums)
        first=0
        second=1
        for i in range(len(nums)):
            if nums[i]<0:
                answer[second]=nums[i]
                second+=2
            else:
                answer[first]=nums[i]
                first+=2
        return answer
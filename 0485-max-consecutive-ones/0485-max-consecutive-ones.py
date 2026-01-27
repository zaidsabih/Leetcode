class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        maximum=0
        for i in nums:
            if i==1:
                count+=1
                maximum=max(count,maximum)
            else:
                count=0
        return maximum
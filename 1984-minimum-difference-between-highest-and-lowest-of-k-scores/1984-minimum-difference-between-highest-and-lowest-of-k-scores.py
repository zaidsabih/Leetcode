class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        i=0
        j=k-1
        minimum=10**5
        while j<len(nums):
            n1=nums[i]
            n2=nums[j]
            sum1=n2-n1
            minimum=min(minimum,sum1)
            i+=1
            j+=1
        return minimum
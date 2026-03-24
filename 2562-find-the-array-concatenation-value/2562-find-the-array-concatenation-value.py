class Solution(object):
    def findTheArrayConcVal(self, nums):
        n=len(nums)
        answer=0
        i=0
        j=len(nums)-1
        l=len(nums)-1
        while i<j:
            answer+=int(str(nums[i])+str(nums[j]))
            i+=1
            j-=1
        if n%2!=0:
            answer+=(nums[l//2])
        return answer
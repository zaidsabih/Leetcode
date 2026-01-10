class Solution(object):
    def majorityElement(self, nums):
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i,j in hash_map.items():
            if j>len(nums)//2:
                return i
        
class Solution(object):
    def sumOfUnique(self, nums):
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        sum1=0
        for key,values in hash_map.items():
            if values==1:
                sum1+=key
        return sum1
class Solution(object):
    def majorityElement(self, nums):
        ans=[]
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for key,value in hash_map.items():
            if value>len(nums)/3:
                ans.append(key)
        return ans


        
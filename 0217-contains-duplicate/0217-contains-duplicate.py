class Solution(object):
    def containsDuplicate(self, nums):
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for key,value in hash_map.items():
            if value!=1:
                return True
        return False

        
class Solution(object):
    def uniqueOccurrences(self, arr):
        hash_map={}
        answer=[]
        for i in arr:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for key,values in hash_map.items():
            if values not in answer:
                answer.append(values)
            else:
                return False
        return True
        
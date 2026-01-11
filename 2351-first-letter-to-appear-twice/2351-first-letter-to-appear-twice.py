class Solution(object):
    def repeatedCharacter(self, s):
        hash_map={}
        for i in s:
            if i not in hash_map:
                hash_map[i]=1
            else:
                return i
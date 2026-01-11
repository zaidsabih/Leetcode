class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        counter=0
        for i in stones:
            if i in jewels:
                counter+=1
        return counter

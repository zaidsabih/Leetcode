class Solution(object):
    def findTheDifference(self, s, t):
        asci1=sum(ord(i) for i in s)
        asci2=sum(ord(j) for j in t)
        return chr(asci2-asci1)
        
        
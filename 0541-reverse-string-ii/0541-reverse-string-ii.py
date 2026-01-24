class Solution(object):
    def reverseStr(self, s, k):
        s=list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k]=reversed(s[i:i+k])
        return "".join(s)
        
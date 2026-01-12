class Solution(object):
    def isSameAfterReversals(self, num):
        copy=num
        answer=0
        while num>0:
            last=num%10
            answer=answer*10+last
            num//=10
        return len(str(copy))==len(str(answer))
        
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        answer=[]
        for i in range(1,int(math.sqrt(num)+1)):
            if num%i==0:
                answer.append(i)

                if i!=num//i:
                    answer.append(num//i)
        sum1=0
        for i in answer:
            if i==num:
                continue
            sum1+=i
        return sum1==num
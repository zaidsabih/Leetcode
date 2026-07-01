class Solution(object):
    def fizzBuzz(self, n):
        answer=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answer.append("FizzBuzz")
            elif i%3==0:
                answer.append("Fizz")
            elif i%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
            
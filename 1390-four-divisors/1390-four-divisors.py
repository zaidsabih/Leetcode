class Solution:
    def sumFourDivisors(self, nums):

        total = 0
        for i in range(len(nums)):
            c,s = self.countt(nums[i])
            if c==4:

                total+=s

        return int(total)


    def countt(self,n):
        count = 0
        summ = 0
        for i in range(1,int(n**0.5)+1):
            j = n//i

            if n%i==0:

                if i==j:

                    count+=1
                    summ+=i

                else:

                    count+=2
                    summ+=i
                    summ+=j

        return (count,summ)

        
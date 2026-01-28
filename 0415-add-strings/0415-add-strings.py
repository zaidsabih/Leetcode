class Solution(object):
    def addStrings(self, num1, num2):
        def addition(num):
            hash_map={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
            result=0
            for i in num:
                result=result*10+hash_map[i]
            return result
        return str(addition(num1)+addition(num2))

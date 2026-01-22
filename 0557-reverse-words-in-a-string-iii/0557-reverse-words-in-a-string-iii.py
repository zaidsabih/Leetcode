class Solution(object):
    def reverseWords(self, s):
        s=s.split(" ")
        answer=[]
        for i in s:
            answer.append(i[::-1])
        return " ".join(answer)
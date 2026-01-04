class Solution(object):
    def reverseOnlyLetters(self, s):
        lst=list(s)
        front=0
        end=len(lst)-1
        while front<end:
            if lst[front].isalpha() and lst[end].isalpha():
                lst[front],lst[end]=lst[end],lst[front]
                front+=1
                end-=1
            elif lst[front].isalpha() and not lst[end].isalpha():
                end-=1
            else:
                front+=1
        return "".join(lst)
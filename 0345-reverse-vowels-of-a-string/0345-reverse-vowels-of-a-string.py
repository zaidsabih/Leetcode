class Solution(object):
    def reverseVowels(self, s):
        vowels=['A','E','I','O','U','a','e','i','o','u']
        lst=list(s)
        front=0
        end=len(lst)-1
        while front<end:
            if lst[front] in vowels and lst[end] in vowels:
                lst[front],lst[end]=lst[end],lst[front]
                front+=1
                end-=1
            elif lst[front] in vowels and lst[end] not in vowels:
                end-=1
            else:
                front+=1
        return "".join(lst)
        


class Solution:
    def makeLargestSpecial(self, s):
        count = 0
        start = 0
        res = []
        
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                res.append("1" + inner + "0")
                start = i + 1
        
        res.sort(reverse=True)
        return "".join(res)
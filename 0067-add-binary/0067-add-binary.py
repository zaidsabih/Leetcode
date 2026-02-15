class Solution:
    def addBinary(self, a, b):
        ans = []
        aInd, bInd = len(a) - 1, len(b) - 1
        carry = 0

        while aInd >= 0 or bInd >= 0 or carry > 0:
            aValue = int(a[aInd]) if aInd >= 0 else 0
            bValue = int(b[bInd]) if bInd >= 0 else 0
            sum_val = aValue + bValue + carry

            # Determine current bit and carry
            if sum_val % 2 == 1:
                ans.append('1')
                carry = 1 if sum_val > 1 else 0
            else:
                ans.append('0')
                carry = 1 if sum_val > 0 else 0

            if aInd >= 0:
                aInd -= 1
            if bInd >= 0:
                bInd -= 1

        return ''.join(reversed(ans))
class Solution:
    def judgeCircle(self, moves):
        c1 = 0  # horizontal
        c2 = 0  # vertical

        for ch in moves:
            if ch == 'L':
                c1 += 1
            elif ch == 'R':
                c1 -= 1
            elif ch == 'U':
                c2 += 1
            elif ch == 'D':
                c2 -= 1

        return c1 == 0 and c2 == 0
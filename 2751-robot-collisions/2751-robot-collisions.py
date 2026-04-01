class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = sorted(list(zip(positions, directions, healths)))
        stack = []

        for bot in robots:
            c = False
            pos, dire, hp = bot
            while dire == 'L' and stack and stack[-1][1] == 'R':
                pos2, dire2, hp2 = stack.pop()
                if hp < hp2:
                    dire = 'R'
                    hp = hp2-1
                    pos = pos2
                elif hp > hp2:
                    hp -= 1
                else:
                    c = True
                    break
            if c: continue
            stack.append((pos, dire, hp))

        d = {pos: hp for pos, _, hp in stack}
        out = []
        for pos in positions:
            if pos in d: out.append(d[pos])
        return out
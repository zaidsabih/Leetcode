class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        kMod = 10 ** 9 + 7

        # extend hFences & vFences
        hFences += [1, m]
        vFences += [1, n]

        # sort increasingly
        hFences = sorted(hFences)
        vFences = sorted(vFences)

        # possible between vertical fences
        vertical_gap = set()
        for i in range(len(vFences)):            # fix the tail index
            for j in range(i):                   # genrate head index
                diff = vFences[i] - vFences[j]
                vertical_gap.add(diff)
            
        edge = -1

        # possible between horizontal fences
        for i in range(len(hFences)):            # fix the tail index
            for j in range(i):                   # genrate head index
                diff = hFences[i] - hFences[j]
                if diff in vertical_gap:
                    edge = max(edge, diff)       # update edge of the block

        # return the area
        return edge * edge % kMod if edge != -1 else -1
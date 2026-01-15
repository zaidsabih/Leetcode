class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        hBars.sort()
        vBars.sort()

        maxiH, maxiV, maxi = 1, 1, 1

        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i-1] == 1:
                maxi += 1
            else:
                maxiH = max(maxiH, maxi)
                maxi = 1
        maxiH = max(maxiH, maxi)

        maxi = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i-1] == 1:
                maxi += 1
            else:
                maxiV = max(maxiV, maxi)
                maxi = 1
        maxiV = max(maxiV, maxi)

        side = min(maxiH+1, maxiV+1)
        return side * side
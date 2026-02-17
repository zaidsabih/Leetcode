class Solution(object):    
    def readBinaryWatch(self, num):
        def dfs(LEDS, idx, hrs, mins, n):
            # base cases
            if hrs >= 12 or mins >= 60:
                return
            if n == 0:
                time = str(hrs) + ":" + "0"*(mins<10) + str(mins)
                result.append(time)
                return

            if idx < len(LEDS):
                if idx <= 3:  # handle hours
                    dfs(LEDS, idx+1, hrs + LEDS[idx], mins, n-1)
                else:  # handle minutes
                    dfs(LEDS, idx+1, hrs, mins + LEDS[idx], n-1)
                dfs(LEDS, idx+1, hrs, mins, n)
        result = []
        LEDS = [
            8, 4, 2, 1,  # top row of watch
            32, 16, 8, 4, 2, 1 # bottom row of watch
        ]
        dfs(LEDS, 0, 0, 0, num)
        
        return result
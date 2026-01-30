class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        index = {}
        for o in original:
            if o not in index:
                index[o] = len(index)
        for c in changed:
            if c not in index:
                index[c] = len(index)

        n = len(index)
        dis = [[float('inf')] * n for _ in range(n)]

        for i in range(len(cost)):
            dis[index[original[i]]][index[changed[i]]] = min(dis[index[original[i]]][index[changed[i]]], cost[i])

        for k in range(n):
            for i in range(n):
                if dis[i][k] < float('inf'):
                    for j in range(n):
                        if dis[k][j] < float('inf'):
                            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        substr_lengths = set(len(o) for o in original)

        dp = [float('inf')] * (len(target) + 1)
        dp[0] = 0

        for i in range(len(target)):
            if dp[i] == float('inf'):
                continue

            if target[i] == source[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for t in substr_lengths:
                if i + t >= len(dp):
                    continue

                sub_source = source[i:i + t]
                sub_target = target[i:i + t]

                c1 = index[sub_source] if sub_source in index else -1
                c2 = index[sub_target] if sub_target in index else -1

                if c1 >= 0 and c2 >= 0 and dis[c1][c2] < float('inf'):
                    dp[i + t] = min(dp[i + t], dp[i] + dis[c1][c2])

        return dp[-1] if dp[-1] != float('inf') else -1
        
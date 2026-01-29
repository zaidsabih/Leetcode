class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        from collections import defaultdict
    # STEP 1
        adj = defaultdict(list)
        for src, dst, cur_cost in zip(original, changed, cost):
            adj[src].append((dst,cur_cost))
    # STEP 2    
        def dijkstra(src):
            heap = [(0, src)]
            min_cost_map = {}
    # STEP 3
            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_map: continue
                min_cost_map[node] = cost
                for nei, nei_cost in adj[node]:
                    heapq.heappush(heap,(cost+nei_cost, nei))
            return min_cost_map
                
    # STEP 4    
        min_cost_maps = {c:dijkstra(c) for c in set(source)}
        res = 0
        for src, dst in zip(source, target):
    # STEP 5
            if dst not in min_cost_maps[src]: return -1
            res += min_cost_maps[src][dst]
        return res
        
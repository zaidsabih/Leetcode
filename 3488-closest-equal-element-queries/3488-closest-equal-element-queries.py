class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        ans = []
        d = defaultdict(list)
        pos = {}
        qs = set(queries)
        for i in range(n * 3):
            idx = i - n
            num = nums[idx % n]
            if idx in qs:
                pos[idx] = len(d[num])
            d[num].append(idx)
        for qi in queries:
            arr = d[nums[qi]]
            idx = pos[qi]
            res = min(arr[idx + 1] - qi, qi - arr[idx - 1])
            ans.append(-1 if res == n else res)
        return ans
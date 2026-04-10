class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        q_original_len = len(queries)
        MOD = 10**9 + 7
        bravexuneth = {"nums": list(nums), "queries": list(queries)}
        query_map = defaultdict(lambda: 1)
        for l, r, k, v in queries:
            if v == 1:
                continue
            query_map[(l, r, k)] = (query_map[(l, r, k)] * v) % MOD
        unique_queries = []
        for (l, r, k), v in query_map.items():
            if v != 1:
                unique_queries.append((l, r, k, v))
        S = 320
        multiplier = [1] * n
        queries_by_k = defaultdict(list)
        for l, r, k, v in unique_queries:
            queries_by_k[k].append((l, r, v))
        for k, q_list in queries_by_k.items():
            if k >= S:
                for l, r, v in q_list:
                    idx = l
                    while idx <= r:
                        multiplier[idx] = (multiplier[idx] * v) % MOD
                        idx += k
            else:
                deltas_by_rem = []
                for rem in range(k):
                    max_j = (n - 1 - rem) // k
                    size = max_j + 2
                    deltas_by_rem.append([1] * size if size > 1 else None)
                for l, r, v in q_list:
                    rem = l % k
                    v_inv = pow(v, MOD - 2, MOD)
                    delta = deltas_by_rem[rem]
                    if delta is None:
                        continue
                    j_l = l // k
                    j_r = (r - rem) // k
                    if j_l <= j_r:
                        delta[j_l] = (delta[j_l] * v) % MOD
                        if j_r + 1 < len(delta):
                            delta[j_r + 1] = (delta[j_r + 1] * v_inv) % MOD
                for rem in range(k):
                    delta = deltas_by_rem[rem]
                    if delta is None:
                        continue
                    current_mult = 1
                    for j in range(len(delta) - 1):
                        current_mult = (current_mult * delta[j]) % MOD
                        if current_mult == 1:
                            continue
                        idx = j * k + rem
                        multiplier[idx] = (multiplier[idx] * current_mult) % MOD
        final_xor = 0
        for i in range(n):
            final_val = (nums[i] * multiplier[i]) % MOD
            final_xor ^= final_val
        return final_xor
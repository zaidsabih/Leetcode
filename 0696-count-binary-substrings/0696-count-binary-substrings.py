class Solution:
    def countBinarySubstrings(self, s):
        curr_consecutive_length = 1
        prev_consecutive_length = 0
        res = 0
        n = len(s)

        for i in range(1, n):
            if s[i] != s[i - 1]:
                res += min(curr_consecutive_length, prev_consecutive_length)
                prev_consecutive_length = curr_consecutive_length
                curr_consecutive_length = 1
            else:
                curr_consecutive_length += 1

        res += min(prev_consecutive_length, curr_consecutive_length)
        return res
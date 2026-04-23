class Solution(object):
    def distance(self, nums):
        n = len(nums)
        res = [0] * n
        # Map each value to a list of its indices
        indices_map = {}
        for i, val in enumerate(nums):
            if val not in indices_map:
                indices_map[val] = []
            indices_map[val].append(i)
        
        # For each group of identical elements
        for val in indices_map:
            indices = indices_map[val]
            m = len(indices)
            
            # Calculate total sum of indices for this value
            total_sum = sum(indices)
            prefix_sum = 0
            
            for j, idx in enumerate(indices):
                # Using the derived formula:
                # Left distances: (count_left * current_idx) - prefix_sum
                # Right distances: (suffix_sum) - (count_right * current_idx)
                
                count_left = j
                count_right = m - 1 - j
                
                suffix_sum = total_sum - prefix_sum - idx
                
                left_dist = (count_left * idx) - prefix_sum
                right_dist = suffix_sum - (count_right * idx)
                
                res[idx] = left_dist + right_dist
                
                # Update prefix_sum for the next index in the group
                prefix_sum += idx
                
        return res
        
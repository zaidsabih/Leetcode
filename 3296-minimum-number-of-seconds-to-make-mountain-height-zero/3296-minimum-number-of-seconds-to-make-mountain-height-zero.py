

class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        # This function checks if all workers can reduce the mountain to 0 or lower within the given time 'limit_time'
        def canFinishInTime(limit_time):
            total_height_reduced = 0  # Total height reduced by all workers
            for worker_time in workerTimes:
                max_height = 0  # The maximum height reduced by this worker
                current_time = worker_time  # The time taken for the first reduction

                # Calculate how many levels this worker can reduce in 'limit_time'
                while limit_time >= current_time:
                    max_height += 1
                    # The time taken increases for each additional level reduced
                    current_time += worker_time * (max_height + 1)
                
                total_height_reduced += max_height

                # If the total height reduced by all workers reaches or exceeds the mountain height, return True
                if total_height_reduced >= mountainHeight:
                    return True

            # If after all workers the total height is still not enough, return False
            return total_height_reduced >= mountainHeight

        # Perform binary search on the time to find the minimum time required to finish
        left, right = 0, workerTimes[0] * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2  # Midpoint of the current search space

            # If workers can finish the mountain reduction within 'mid' time, search the left half
            if canFinishInTime(mid):
                right = mid
            else:
                # Otherwise, search the right half
                left = mid + 1

        # Return the minimum time required to reduce the mountain
        return left

# Time Complexity:
# The overall time complexity is O(n * log(T)), where:
# - n is the number of workers (i.e., len(workerTimes)).
# - T is the maximum time we are searching through, initially set to workerTimes[0] * mountainHeight * (mountainHeight + 1) / 2.
#   We perform a binary search over this time, which takes O(log(T)).
# - Inside each binary search step, we run the canFinishInTime function, which iterates over the workers (O(n)).

# Space Complexity:
# The space complexity is O(1), as we are using only constant extra space to store variables like `total_height_reduced`, `max_height`, and loop variables.
# No extra space is used for data structures that scale with input size.
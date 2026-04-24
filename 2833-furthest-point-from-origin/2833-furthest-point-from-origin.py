class Solution:
    def furthestDistanceFromOrigin(self, moves):
        left = moves.count('L')
        right = moves.count('R')
        blanks = moves.count('_')

        return abs(left - right) + blanks
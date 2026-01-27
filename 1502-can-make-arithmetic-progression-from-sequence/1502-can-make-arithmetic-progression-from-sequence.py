class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        difference=arr[1]-arr[0]
        for i in range(2,len(arr)):
            current_difference=arr[i]-arr[i-1]
            if current_difference==difference:
                continue
            else:
                return False
        return True
class Solution(object):
    def minimumAbsDifference(self, arr):
        minimum=10**6
        result=[]
        arr.sort()
        for i in range(1,len(arr)):
            difference=arr[i]-arr[i-1]
            if minimum>difference:
                result=[[arr[i-1],arr[i]]]
                minimum=difference
            elif minimum==difference:
                result.append([arr[i-1],arr[i]])
        return result
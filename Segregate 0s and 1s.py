##Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

class Solution:
    def segregate0and1(self, arr):
        end=len(arr)-1
        start=0
        while start<end:
            if arr[start]==0:
                start+=1
            if arr[end]==1:
                end-=1
            else:
                arr[start],arr[end]=arr[end],arr[start]
        return arr

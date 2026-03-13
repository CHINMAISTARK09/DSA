##Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 1


class Solution:
    def maxWater(self, arr):
        prefix_max=[0]*len(arr) ## To Store the max height of building to the left at the curr index
        suffix_max=[0]*len(arr) ## To Store the max height of building to the right at the curr index
        if len(arr)==1 or len(arr)==0:
            return 0
        prefix_max[0]=arr[0] ## Max height of building to the left at first index will be the curr building height
        suffix_max[len(arr)-1]=arr[len(arr)-1] ## Max height of building to the left at last index will be the curr building height
        left=1
        right=len(arr)-2
        while left<len(arr) and right>=0:
            prefix_max[left]=max(arr[left],prefix_max[left-1])
            suffix_max[right]=max(arr[right],suffix_max[right+1])
            left+=1
            right-=1
        total_water=0
        for i in range(1,len(arr)-1):
            curr_water=min(prefix_max[i],suffix_max[i])-arr[i]
            total_water+=curr_water
        return total_water


## Time Complexity O(N) Space Complexity O(N)

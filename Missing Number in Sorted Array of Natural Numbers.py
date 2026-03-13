##Given a sorted array arr[] of n-1 integers, these integers are in the range of 1 to n. There are no duplicates in the array. One of the integers is missing in the array. Find the missing integer.1

class Solution:
    def missingNumber(self, arr):
        left=0
        right=len(arr)-1
        mid=(left+right)//2            -----just to satisfy the case when there is no missing number you can remove this part if there is atleast one missing number
        if arr[right]==right+1:        -----just to satisfy the case when there is no missing number you can remove this part if there is atleast one missing number
            return arr[right]+1        -----just to satisfy the case when there is no missing number you can remove this part if there is atleast one missing number
        while left<right:
            mid=(left+right)//2
            if arr[mid]==mid+1:
                left=mid+1
            else:
                right=mid
        return left+1

## Time Complexity O(log N) Space Complexity O(1)

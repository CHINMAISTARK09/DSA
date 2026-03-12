##Given an array arr[] and an integer target. You have to return the pair of elements which sum upto target. You cannot use the same element twice.
##Note: Inputs are given such that only one valid answer exists.


## Time Complexity O(N) and Space Complexity O(N)
class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        seen=set()
        for elem in arr:
            if target-elem in seen:
                return [target-elem,elem]
            else:
                seen.add(elem)
        return []

## Using set the search takes O(1) if we use List it takes O(N) to search

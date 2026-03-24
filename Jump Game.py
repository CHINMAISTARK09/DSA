##Given a array of positive integers arr, where each element denotes the maximum length of jump you can cover. Find out if you can make it to the last index starting from the first index of the list, return true if you can reach the last index.

class Solution:
    # Function to check if we can reach the last index from the 0th index.
    def canReach(self, arr):
        if len(arr)==0 or (len(arr)==1 and arr[0]!=1):
            return True
        final=len(arr)-1
        before=len(arr)-1
        while before>=0:
            if before+arr[before]>=final:
                final=before
            before-=1
        if final==0:
            return True

Time Complexity: O(n)
Auxiliary Space: O(1)

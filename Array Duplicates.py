##Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

##Note: You can return the elements in any order but the driver code will print them in sorted order.

class Solution:
    def findDuplicates(self, arr):
        result=[]
        for i in range(len(arr)):
            index=abs(arr[i])-1
            if arr[index] <0:
                result.append(abs(arr[i]))
            else:       
                arr[index]=-arr[index]
        return result

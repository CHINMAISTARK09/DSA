##Given a A X B matrix with your initial position at the top-left cell, find the number of possible unique paths to reach the bottom-right cell of the matrix from the initial position.

##Note: Possible moves can be either down or right at any point in time, i.e., we can move to matrix[i+1][j] or matrix[i][j+1] from matrix[i][j].


class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        dp_arr=[[0]*b for i in range(a)]
        for i in range(len(dp_arr)):
            for j in range(len(dp_arr[0])):
                if i==0 or j ==0:
                    dp_arr[i][j]=1
                else:
                    dp_arr[i][j]=dp_arr[i-1][j]+dp_arr[i][j-1]
        return dp_arr[a-1][b-1]
        #code here

class Solution:
    def makelandtowater(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='W':
            return 
        grid[i][j]='W'
        self.makelandtowater(grid,i,j-1)
        self.makelandtowater(grid,i,j+1)
        self.makelandtowater(grid,i-1,j)
        self.makelandtowater(grid,i+1,j)
        self.makelandtowater(grid,i-1,j-1)
        self.makelandtowater(grid,i+1,j+1)
        self.makelandtowater(grid,i-1,j+1)
        self.makelandtowater(grid,i+1,j-1)
    def numIslands(self, grid):
        island=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='L':
                    island+=1
                    self.makelandtowater(grid,i,j)
        return island

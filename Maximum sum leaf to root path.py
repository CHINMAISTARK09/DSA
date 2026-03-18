Given a Binary Tree, find the maximum sum path from a leaf to root.

class Solution:
    def maxPathSum(self, root):
        res = float('-inf')
        def dfs(node,total):
            nonlocal res
            if not node:
                return
            total+=node.data
            if not node.left and not node.right:
                res=max(res,total)
            dfs(node.left,total)
            dfs(node.right,total)
        dfs(root,0)  
        return res

Time Complexity: O(n) , where n = number of nodes
Auxiliary Space: O(1)

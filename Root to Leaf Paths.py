Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.


class Solution:
    def Paths(self, root):
        res=[]
        
        def dfs(node,path):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:
                res.append(path[:])  --if we store path directly, every time we run pop on path, the change happens in the result array aswell which has the path as subarray in it.
            dfs(node.left,path),dfs(node.right,path)
            path.pop()
        
        dfs(root,[])    
        return res    

##Time Complexity: O(n) and Auxiliary Space: O(h)

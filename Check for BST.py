Given the root of a binary tree. Check whether it is a BST or not.

A BST is defined as follows:

The left subtree of a node contains only nodes with data less than the node's data.
The right subtree of a node contains only nodes with data greater than the node's data.
Both the left and right subtrees must also be binary search trees.
Note: We are considering that BSTs can not contain duplicate Nodes.


class Solution:
    def isBST(self, root):
        if not root:
            return
        def dfs(low,node,high):
            if not node:
                return True
            if not low<node.data<high:
                return False
            return(
                dfs(low,node.left,node.data) 
                and 
                dfs(node.data,node.right,high)
                )
        return dfs(float('-inf'),root,float('inf'))    

Time Complexity: O(n)
Auxiliary Space: O(h)

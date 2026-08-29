class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Base case: if the tree is empty, its depth is 0
        if not root:
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth is the greater of the two depths, plus 1 for the root node
        return max(left_depth, right_depth) + 1
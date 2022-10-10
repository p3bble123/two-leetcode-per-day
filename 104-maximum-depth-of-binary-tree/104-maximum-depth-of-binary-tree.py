# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.getMaxDepth(root)

    def getMaxDepth(self, node):
        if node == None:
            return 0

        if node.right == None and node.left == None:
            return 1

        left = 0 if node.left == None else self.getMaxDepth(node.left)
        right = 0 if node.right == None else self.getMaxDepth(node.right)

        return max(left, right)+1

# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.compareDepth(root) == -1:
            return False
        return True

    def compareDepth(self, node):
        if node == None:
            return 0
        if node.right == None and node.left == None:
            return 1

        leftDepth = self.compareDepth(node.left)
        rightDepth = self.compareDepth(node.right)

        if leftDepth == -1 or rightDepth == -1:
            return -1
        if abs(leftDepth -rightDepth) > 1:
            return -1

        curDepth = max(leftDepth, rightDepth) + 1
        return curDepth
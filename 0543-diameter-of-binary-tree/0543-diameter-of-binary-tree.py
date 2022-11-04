# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 0
        return self.getMaxDiameter(root, root, 0)

    def getMaxDiameter(self, root, node, maxDiameter):
        if node == None:
            return 0

        if node.right == None and node.left == None:
            print(node.val, " is leaf => return 1")
            return 1

        left = self.getMaxDiameter(root, node.left, maxDiameter)
        right = self.getMaxDiameter(root, node.right, maxDiameter)

        self.maxDiameter = max(self.maxDiameter, left + right)
        maxDepth = max(left, right)

        if node is root:
            return self.maxDiameter
        return maxDepth + 1

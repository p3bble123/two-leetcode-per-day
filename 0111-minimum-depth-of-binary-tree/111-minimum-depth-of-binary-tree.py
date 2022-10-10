# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMinDepth(root)

    def getMinDepth(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 1

        if node.left == None and node.right != None:
            leftDepth = 105
            rightDepth = self.getMinDepth(node.right)
        elif node.right == None and node.left != None:
            leftDepth = self.getMinDepth(node.left)
            rightDepth = 105
        else:
            leftDepth = self.getMinDepth(node.left)
            rightDepth = self.getMinDepth(node.right)

        return min(leftDepth, rightDepth)+1

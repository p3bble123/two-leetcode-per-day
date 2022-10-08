# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertChildren(root)
        return root

    def invertChildren(self, node):
        if node == None:
            return
        if (node.left == None) and (node.right == None):
            return

        self.invertChildren(node.left)
        self.invertChildren(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

        return

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = []
        self.visitPostorder(root, visit)

        return visit

    def visitPostorder(self, node, visit):
        if node == None:
            return

        if node.left != None:
            self.visitPostorder(node.left, visit)
        if node.right != None:
            self.visitPostorder(node.right, visit)

        visit.append(node.val)

        return
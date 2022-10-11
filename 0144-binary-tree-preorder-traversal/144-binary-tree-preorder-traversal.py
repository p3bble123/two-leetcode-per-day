# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = []
        self.visitPreorder(root, visit)

        return visit

    def visitPreorder(self, node, visit):
        if node == None:
            return
        if node.left == None and node.right == None:
            visit.append(node.val)
            return

        visit.append(node.val)
        self.visitPreorder(node.left, visit)
        self.visitPreorder(node.right, visit)

        return
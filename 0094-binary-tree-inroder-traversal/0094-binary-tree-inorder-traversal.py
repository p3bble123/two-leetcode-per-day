# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorderTraversal: 1. visit left node, 2. visit self, 3. visit right(recurse 1, 2)
        visited = []
        self.visitNodes(root, visited)

        return visited

    def visitNodes(self, node, visited):
        if node == None:
            return

        if node.right == None and node.left == None:
            visited.append(node.val)
            return

        self.visitNodes(node.left, visited)
        visited.append(node.val)
        self.visitNodes(node.right, visited)

        return

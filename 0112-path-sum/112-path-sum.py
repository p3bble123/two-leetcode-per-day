# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.getSum(root, targetSum)

    def getSum(self, node, target):
        if node == None:
            return False

        if node.right == None and node.left == None:
            if node.val == target:
                return True
            else:
                return False

        leftSum = self.getSum(node.left, target-node.val)
        rightSum = self.getSum(node.right, target-node.val)

        return (leftSum or rightSum)
# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(nums)

    def buildBST(self, nums):
        mid = len(nums)//2

        if mid < 0 or mid >= len(nums):
            return None

        node = TreeNode(nums[mid])
        node.left = self.buildBST(nums[:mid])
        node.right = self.buildBST(nums[mid+1:])

        return node
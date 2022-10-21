# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/all-possible-full-binary-trees/solutions/2229147/python-recursive/

class Solution:
    def allPossibleFBT(self, n: int, memo={1: [TreeNode()]}) -> List[Optional[TreeNode]]:
        if n in memo:
            return memo[n]

        result = []
        for m in range(1, n, 2):
            left_list = self.allPossibleFBT(m)
            right_list = self.allPossibleFBT(n - m - 1)
            for left in left_list:
                for right in right_list:
                    result.append(TreeNode(0, left, right))

        memo[n] = result
        return result
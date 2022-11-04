# 내풀이랑 다른 완전 단순하고 좋은 풀이 ㅠㅠ
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/152682/python-simple-recursive-solution-with-detailed-explanation/?orderBy=most_votes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pRoute = self.getNodeSearchRoute(root, p)
        qRoute = self.getNodeSearchRoute(root, q)
        return self.getCommonAncestor(pRoute, qRoute)

    def getNodeSearchRoute(self, node, target):
        if node == None:
            return []

        if node == target:
            return [node]

        if node.val > target.val:
            leftCheck = self.getNodeSearchRoute(node.left, target)
            if len(leftCheck) > 0:
                leftCheck.append(node)
            return leftCheck

        if node.val < target.val:
            rightCheck = self.getNodeSearchRoute(node.right, target)
            if len(rightCheck) > 0:
                rightCheck.append(node)
            return rightCheck

    def getCommonAncestor(self, pRoute, qRoute):
        pLength = len(pRoute)
        qLength = len(qRoute)

        if qLength > pLength:
            qRoute = qRoute[(qLength - pLength):]
        if pLength > qLength:
            pRoute = pRoute[(pLength - qLength):]

        for i in range(pLength):
            if pRoute[i] == qRoute[i]:
                return pRoute[i]

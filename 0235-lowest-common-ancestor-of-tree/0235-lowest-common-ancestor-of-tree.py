# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pRoute = self.getNodeSearchRoute(root, p)
        qRoute = self.getNodeSearchRoute(root, q)
        return self.getCommonAncestor(pRoute, qRoute)


    def getNodeSearchRoute(self, curNode, target):
        if curNode == None:
            return []

        if curNode == target:
            return [curNode]

        checkLeft = self.getNodeSearchRoute(curNode.left, target)
        if len(checkLeft) != 0:
            checkLeft.append(curNode)
            return checkLeft

        checkRight = self.getNodeSearchRoute(curNode.right, target)
        if len(checkRight) != 0:
            checkRight.append(curNode)
            return checkRight

        return []


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

        return None
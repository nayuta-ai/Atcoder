# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left==-1 or right==-1 or abs(right-left)>1:
                return -1
            return 1+max(right,left)
        return check(node)!=-1
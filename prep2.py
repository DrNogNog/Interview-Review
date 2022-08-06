# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as que
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = que([(root,1)])
        res = []
        while q:
            u, coord = q.popleft()
            res.append(coord)
            if u.left:
                q.append((u.left, 2*coord))
            if u.right:
                q.append((u.right, 2*coord+1))
        return len(res) == res[-1]
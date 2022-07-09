class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0
        def dfs(node, curSum):
            if not node:
                return
            #Traverse Entire Right Subtree
            nonlocal curSum
            dfs(node.right)
            tmp = node.val
            node.val += curSum
            curSum += node.val
            dfs(node.left)
        dfs(root)
        return root
# O(n)
# O(1)
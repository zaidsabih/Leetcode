# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total, sub = 0, []
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sub.append(s)
            return s
        total = dfs(root)
        return max(x * (total - x) for x in sub) % (10**9 + 7)
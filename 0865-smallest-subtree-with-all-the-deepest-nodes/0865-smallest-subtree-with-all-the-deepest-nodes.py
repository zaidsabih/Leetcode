class Solution:
    def dfs(self, root):
        if not root:
            return (0, None)

        ld, ln = self.dfs(root.left)
        rd, rn = self.dfs(root.right)

        if ld > rd:
            return (ld + 1, ln)
        if rd > ld:
            return (rd + 1, rn)

        return (ld + 1, root)

    def subtreeWithAllDeepest(self, root):
        return self.dfs(root)[1]

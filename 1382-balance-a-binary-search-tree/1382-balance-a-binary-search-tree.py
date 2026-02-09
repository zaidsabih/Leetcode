class Solution:
    def __init__(self):
        self.vals = []

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.vals.append(root.val)
        self.inorder(root.right)

    def build(self, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(self.vals[mid])

        root.left = self.build(left, mid - 1)
        root.right = self.build(mid + 1, right)

        return root

    def balanceBST(self, root):
        self.inorder(root)
        return self.build(0, len(self.vals) - 1)
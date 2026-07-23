class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False

            return check(a.left, b.right) and check(a.right, b.left)

        return check(root.left, root.right)
        
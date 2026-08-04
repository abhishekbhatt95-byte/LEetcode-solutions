from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])
        leftToRight = True

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if leftToRight:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level)
            leftToRight = not leftToRight

        return ans
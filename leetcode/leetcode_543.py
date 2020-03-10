# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0

        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            # 更新res
            self.res = max(l+r, self.res)
            # 返回高度
            return max(l, r)+1
            
        dfs(root)
        return self.res

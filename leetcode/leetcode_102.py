# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        layer = [root]
        res = []
        while len(layer):
            this_res = []
            next_l = []
            for n in layer:
                this_res.append(n.val)
            if n.left:
                next_l.append(n.left)
            if n.right:
                next_l.append(n.right)
            res.append(this_res)
            layer = next_l
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        helper = [root]
        res = []
        while helper:
            tmp1 = []
            tmp2 = []
            for node in helper:
                tmp1.append(node.val)
                if node.left:
                    tmp2.append(node.left)
                if node.right:
                    tmp2.append(node.right)
            res.append(tmp1)
            helper = tmp2
        return res


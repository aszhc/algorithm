#!/usr/bin/python3
class Node:
    """节点类"""

    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""

    def __init__(self):
        self.root = None

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                else:
                    queue.append(cur.lchild)
                if cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.rchild)

    def preorder(self, root):
        """先序遍历"""
        if root is None:
            return
        print(root.elem, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def postorder(self, root):
        """后序遍历"""
        if root is None:
            return
        self.preorder(root.lchild)
        self.preorder(root.rchild)
        print(root.elem, end=" ")

    def inorder(self, root):
        """中序遍历"""
        if root is None:
            return
        self.preorder(root.lchild)
        print(root.elem, end=" ")
        self.preorder(root.rchild)

    def breadth_travel(self):
        """广度广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem, end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


if __name__ == "__main__":
    tree = Tree()
    tree.add('1')
    tree.add('2')
    tree.add('3')
    tree.add('4')
    tree.add('5')
    tree.add('6')
    tree.preorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.breadth_travel()

import unittest
from main import Solution

obj = Solution()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


class TreeTests(unittest.TestCase):

    def test_1(self):
        """Works for Binary Search Tree of 1, 2, and 3 levels"""
        root = Node(8)
        self.assertEqual(obj.maxDepth(root), 1)
        insert(root, Node(3))
        insert(root, Node(10))
        self.assertEqual(obj.maxDepth(root), 2)
        insert(root, Node(14))
        self.assertEqual(obj.maxDepth(root), 3)
        #          8
        #        /   \
        #       3     10
        #      / \      \
        #               14

    def test_2(self):
        """Works for Binary Tree with 0 levels"""
        root = None
        self.assertEqual(obj.maxDepth(root), 0)


if __name__ == '__main__':
    unittest.main()

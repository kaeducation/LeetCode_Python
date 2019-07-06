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
        """Inverts tree"""
        root = Node(8)
        insert(root, Node(3))
        insert(root, Node(10))
        insert(root, Node(1))
        insert(root, Node(6))
        insert(root, Node(14))
        #          8
        #        /   \
        #       3     10
        #      / \      \
        #     1   6      14
        obj.invertTree(root)
        self.assertEqual(root.val, 8)

        self.assertEqual(root.left.val, 10)
        self.assertEqual(root.right.val, 3)

        self.assertEqual(root.left.left.val, 14)
        self.assertEqual(root.right.right.val, 1)

    def test_2(self):
        """Inverts empty tree"""
        root = None
        obj.invertTree(root)
        self.assertEqual(root, None)

    def test_3(self):
        """Inverts tree with only one node"""
        root = Node(8)
        obj.invertTree(root)
        self.assertEqual(root.val, 8)


if __name__ == '__main__':
    unittest.main()

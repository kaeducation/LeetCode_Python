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
        """Returns True for valid BST."""
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
        self.assertEqual(obj.isValidBST(root), True)

    def test_2(self):
        """Returns True for empty BST."""
        self.assertEqual(obj.isValidBST(None), True)

    def test_3(self):
        """Returns False for invalid BST."""
        root = Node(8)
        insert(root, Node(3))
        insert(root, Node(10))
        root.right.left = Node(6)
        #          8
        #        /   \
        #       3     10
        #      / \   /
        #           6
        self.assertEqual(obj.isValidBST(root), False)


if __name__ == '__main__':
    unittest.main()

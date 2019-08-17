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
        """Returns True correctly."""
        root1 = Node(8)
        insert(root1, Node(3))
        insert(root1, Node(10))
        insert(root1, Node(1))
        insert(root1, Node(6))
        insert(root1, Node(14))
        #          8
        #        /   \
        #       3     10
        #      / \      \
        #     1   6      14

        root2 = Node(3)
        insert(root2, Node(1))
        insert(root2, Node(6))
        #       3
        #      / \
        #     1   6
        self.assertEqual(obj.isSubtree(root1, root2), True)

        self.assertEqual(obj.isSubtree(root1, Node(1)), True)
        self.assertEqual(obj.isSubtree(root1, Node(14)), True)

    def test_2(self):
        """Returns False correctly."""
        root1 = Node(8)
        insert(root1, Node(3))
        insert(root1, Node(10))
        insert(root1, Node(1))
        insert(root1, Node(6))
        insert(root1, Node(14))
        insert(root1, Node(7))
        #          8
        #        /   \
        #       3     10
        #      / \      \
        #     1   6      14
        #          \
        #           7

        root2 = Node(3)
        insert(root2, Node(1))
        insert(root2, Node(6))

        self.assertEqual(obj.isSubtree(root1, root2), False)
        self.assertEqual(obj.isSubtree(root1, Node(13)), False)


if __name__ == '__main__':
    unittest.main()

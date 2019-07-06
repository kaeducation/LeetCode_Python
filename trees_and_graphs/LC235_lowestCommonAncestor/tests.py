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
        """Returns lowest common ancestor."""
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
        node_3 = root.left
        node_10 = root.right
        node_14 = root.right.right

        self.assertEqual(obj.lowestCommonAncestor(root, node_3, node_10), root)
        self.assertEqual(obj.lowestCommonAncestor(
            root, node_14, node_10), node_10)


if __name__ == '__main__':
    unittest.main()

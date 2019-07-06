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
        """returns True for same trees"""
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

        root2 = Node(8)
        insert(root2, Node(3))
        insert(root2, Node(10))
        insert(root2, Node(1))
        insert(root2, Node(6))
        insert(root2, Node(14))
        #          8
        #        /   \
        #       3     10
        #      / \      \
        #     1   6      14

        self.assertEqual(obj.isSameTree(root, root2), True)

    def test_2(self):
        """returns False for same trees"""
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

        root2 = Node(8)
        insert(root2, Node(3))
        insert(root2, Node(10))
        insert(root2, Node(1))
        insert(root2, Node(6))
        insert(root2, Node(144))
        #          8
        #        /   \
        #       3     10
        #      / \      \
        #     1   6      144

        self.assertEqual(obj.isSameTree(root, root2), False)


if __name__ == '__main__':
    unittest.main()

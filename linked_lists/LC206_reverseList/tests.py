import unittest
from main import Solution

obj = Solution()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """reverses the list"""
        head = ListNode("A")
        b_node = ListNode("B")
        head.next = b_node

        self.assertEqual(obj.reverseList(head), b_node)
        self.assertEqual(b_node.next, head)
        self.assertEqual(head.next, None)


if __name__ == '__main__':
    unittest.main()

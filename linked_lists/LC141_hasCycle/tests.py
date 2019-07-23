import unittest
from main import Solution

obj = Solution()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """Return False on empty list"""
        self.assertEqual(obj.hasCycle({}), False)

    def test_2(self):
        """Returns True for circular linked lists"""
        a_node = ListNode("A")
        b_node = ListNode("B")
        c_node = ListNode("C")
        d_node = ListNode("D")
        a_node.next = b_node
        b_node.next = c_node
        c_node.next = d_node
        d_node.next = b_node

        self.assertEqual(obj.hasCycle(a_node), True)

    def test_3(self):
        """Returns False for non circular linked lists"""
        a_node = ListNode("A")
        b_node = ListNode("B")
        c_node = ListNode("C")
        a_node.next = b_node
        b_node.next = c_node

        self.assertEqual(obj.hasCycle(a_node), False)


if __name__ == '__main__':
    unittest.main()

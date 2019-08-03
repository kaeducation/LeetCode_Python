import unittest
from main import Solution

obj = Solution()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """Work for LL with odd number of nodes"""
        a_node = ListNode("A")
        b_node = ListNode("B")
        c_node = ListNode("C")

        a_node.next = b_node
        b_node.next = c_node

        self.assertEqual(obj.middleNode(a_node), b_node)

    def test_2(self):
        """Work for LL with even number of nodes"""
        a_node = ListNode("A")
        curr = a_node

        for char in ["B", "C", "D"]:
            curr.next = ListNode(char)
            curr = curr.next

        self.assertEqual(obj.middleNode(a_node).val, "C")


if __name__ == '__main__':
    unittest.main()

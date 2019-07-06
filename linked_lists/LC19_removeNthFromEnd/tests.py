import unittest
from main import Solution, ListNode

obj = Solution()


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """removeNthFromEnd([a, b, c, d, e], 2) becomes [a, b, c, e]"""
        a_node = ListNode("A")
        b_node = ListNode("B")
        c_node = ListNode("C")
        d_node = ListNode("D")
        e_node = ListNode("E")

        a_node.next = b_node
        b_node.next = c_node
        c_node.next = d_node
        d_node.next = e_node

        self.assertEqual(obj.removeNthFromEnd(a_node, 2), a_node)
        self.assertEqual(c_node.next, e_node)

        counter = 0
        curr = a_node
        while curr:
            curr = curr.next
            counter += 1

        self.assertEqual(counter, 4)

    def test_2(self):
        """removeNthFromEnd([a], 1) becomes []"""
        a_node = ListNode("A")

        self.assertEqual(obj.removeNthFromEnd(a_node, 1), None)


if __name__ == '__main__':
    unittest.main()

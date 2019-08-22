import unittest
from main import Solution, Node

obj = Solution()


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """Works when random pointers point to valid node"""
        one_node = Node(1, None, None)
        two_node = Node(2, None, None)

        one_node.next = two_node
        one_node.random = two_node
        two_node.random = two_node

        res_head = obj.copyRandomList(one_node)
        self.assertEqual(res_head == one_node, False)
        self.assertEqual(res_head.next == two_node, False)

        self.assertEqual(res_head.random == res_head.next, True)
        self.assertEqual(res_head.next.random == res_head.next, True)

        curr = res_head
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 2])

    def test_2(self):
        """Works when random pointers point to None"""
        one_node = Node(1, None, None)
        two_node = Node(2, None, None)

        one_node.next = two_node
        one_node.random = two_node
        two_node.random = None

        res_head = obj.copyRandomList(one_node)
        self.assertEqual(res_head == one_node, False)
        self.assertEqual(res_head.next == two_node, False)

        self.assertEqual(res_head.random == res_head.next, True)
        self.assertEqual(res_head.next.random == None, True)

        curr = res_head
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 2])

    def test_3(self):
        """Works on empty Linked List"""

        res_head = obj.copyRandomList(None)
        self.assertEqual(res_head, None)


if __name__ == '__main__':
    unittest.main()

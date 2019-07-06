import unittest
from main import Solution, ListNode

obj = Solution()


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """[1,3], [2,4,6] returns head of [1,2,3,4,6]"""
        one_node = ListNode(1)
        three_node = ListNode(3)
        one_node.next = three_node

        two_node = ListNode(2)
        four_node = ListNode(4)
        six_node = ListNode(6)
        two_node.next = four_node
        four_node.next = six_node

        res_linked_list = obj.mergeTwoLists(one_node, two_node)

        curr = res_linked_list
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 2, 3, 4, 6])

    def test_2(self):
        """[1,3], [] returns head of [1,3]"""
        one_node = ListNode(1)
        three_node = ListNode(3)
        one_node.next = three_node

        res_linked_list = obj.mergeTwoLists(one_node, None)

        curr = res_linked_list
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 3])

    def test_3(self):
        """[], [] returns head of []"""
        res_linked_list = obj.mergeTwoLists(None, None)

        curr = res_linked_list
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [])


if __name__ == '__main__':
    unittest.main()

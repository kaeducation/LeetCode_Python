import unittest
from main import Solution

obj = Solution()


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListTests(unittest.TestCase):

    def test_1(self):
        """[1,2,3,4,5,6] returns head of [1, 6, 2, 5, 3, 4]"""
        head = ListNode(1)
        curr = head
        for i in range(2, 7):
            curr.next = ListNode(i)
            curr = curr.next

        obj.reorderList(head)
        curr = head
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 6, 2, 5, 3, 4])

    def test_2(self):
        """[1,2,3] returns head of [1,3,2]"""
        head = ListNode(1)
        curr = head
        for i in range(2, 4):
            curr.next = ListNode(i)
            curr = curr.next

        obj.reorderList(head)
        curr = head
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 3, 2])

    def test_3(self):
        """No errors on empty list"""
        head = None

        obj.reorderList(head)

        self.assertEqual(head, None)


if __name__ == '__main__':
    unittest.main()

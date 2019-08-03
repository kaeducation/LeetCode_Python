import unittest
from main import Solution, ListNode

obj = Solution()


class HeapTests(unittest.TestCase):

    def test_1(self):
        """[[3,5,7], [0,6], [0,6,28]] returns head of [0,0,3,5,6,6,7,28]"""
        head1 = ListNode(3)
        curr = head1
        for num in [5, 7]:
            curr.next = ListNode(num)
            curr = curr.next

        head2 = ListNode(0)
        curr = head2
        for num in [6]:
            curr.next = ListNode(num)
            curr = curr.next

        head3 = ListNode(0)
        curr = head3
        for num in [6, 28]:
            curr.next = ListNode(num)
            curr = curr.next

        res_list_head = obj.mergeKLists([head1, head2, head3])
        curr = res_list_head
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [0, 0, 3, 5, 6, 6, 7, 28])

    def test_2(self):
        """[[]] returns None"""
        res_list_head = obj.mergeKLists([None])
        self.assertEqual(res_list_head, None)


if __name__ == '__main__':
    unittest.main()

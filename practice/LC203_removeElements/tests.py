import unittest
from main import Solution, ListNode

obj = Solution()


class PracticeTests(unittest.TestCase):

    def test_1(self):
        """[1,2,3,4,5,6], val = 6 returns [1,2,3,4,5]"""
        head = ListNode(1)
        curr = head
        for i in range(2, 7):
            curr.next = ListNode(i)
            curr = curr.next

        obj.removeElements(head, 6)
        curr = head
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [1, 2, 3, 4, 5])

    def test_2(self):
        """[1,1], val = 1 returns []"""
        head = ListNode(1)
        curr = head
        curr.next = ListNode(1)

        curr = obj.removeElements(head, 1)
        res_list = []
        while curr:
            res_list.append(curr.val)
            curr = curr.next

        self.assertEqual(res_list, [])


if __name__ == '__main__':
    unittest.main()

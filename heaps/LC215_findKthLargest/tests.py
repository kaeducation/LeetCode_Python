import unittest
from main import Solution

obj = Solution()


class HeapTests(unittest.TestCase):

    def test_1(self):
        """findKthLargest works"""
        self.assertEqual(obj.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


if __name__ == '__main__':
    unittest.main()

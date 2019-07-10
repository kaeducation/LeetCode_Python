import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """[1] returns 1"""
        self.assertEqual(obj.findMin([1]), 1)

    def test_2(self):
        """[1, 2] returns 1"""
        self.assertEqual(obj.findMin([1, 2]), 1)

    def test_3(self):
        """[4,5,6,7,0,1,2] returns 0"""
        self.assertEqual(obj.findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_4(self):
        """[5, 1, 2, 3, 4] returns 1"""
        self.assertEqual(obj.findMin([5, 1, 2, 3, 4]), 1)

    def test_5(self):
        """[2,3,4,5,6,1] returns 1"""
        self.assertEqual(obj.findMin([2, 3, 4, 5, 6, 1]), 1)


if __name__ == '__main__':
    unittest.main()

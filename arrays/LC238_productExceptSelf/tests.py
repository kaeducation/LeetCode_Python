import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """productExceptSelf([1,2,3,4]) returns [24, 12, 8, 6]"""
        self.assertEqual(obj.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_2(self):
        """productExceptSelf([] returns [])"""
        self.assertEqual(obj.productExceptSelf([]), [])


if __name__ == '__main__':
    unittest.main()

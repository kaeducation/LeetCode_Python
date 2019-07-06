import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """returns True for Arrays with duplicate values"""
        self.assertEqual(obj.containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(obj.containsDuplicate(
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)

    def test_2(self):
        """returns False for Arrays with NO duplicate values"""
        self.assertEqual(obj.containsDuplicate([1, 2, 3, 4]), False)


if __name__ == '__main__':
    unittest.main()

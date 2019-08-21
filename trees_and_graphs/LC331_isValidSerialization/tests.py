import unittest
from main import Solution

obj = Solution()


class TreeTests(unittest.TestCase):

    def test_1(self):
        """Returns True correctly"""
        self.assertEqual(obj.isValidSerialization("9,#,92,#,#"), True)

    def test_2(self):
        """Returns False correctly"""
        self.assertEqual(obj.isValidSerialization("#,#,3,5,#"), False)


if __name__ == '__main__':
    unittest.main()

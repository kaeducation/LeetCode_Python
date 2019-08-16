import unittest
from main import Solution

obj = Solution()


class PracticeTests(unittest.TestCase):

    def test_1(self):
        """returns True correctly"""
        self.assertEqual(obj.backspaceCompare("y#fo##f", "y#f#o##f"), True)
        self.assertEqual(obj.backspaceCompare("a##c", "#a#c"), True)

    def test_2(self):
        """returns False correctly"""
        self.assertEqual(obj.backspaceCompare("a#c", "b"), False)


if __name__ == '__main__':
    unittest.main()

import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """[-2, 3, -4] --> 24"""
        self.assertEqual(obj.maxProduct([-2, 3, -4]), 24)

    def test_2(self):
        """[-4, -3, -2] --> 12"""
        self.assertEqual(obj.maxProduct([-4, -3, -2]), 12)

    def test_3(self):
        """[-2, -3, 7] --> 42"""
        self.assertEqual(obj.maxProduct([-2, -3, 7]), 42)

    def test_4(self):
        """[2, 3, -2, 4]  --> 6"""
        self.assertEqual(obj.maxProduct([2, 3, -2, 4]), 6)

    def test_5(self):
        """[-1,-2,-9,-6] --> 108"""
        self.assertEqual(obj.maxProduct([-1, -2, -9, -6]), 108)

    def test_6(self):
        """[1,2,-1,-2,2,1,-2,1,4,-5,4] --> 1280"""
        self.assertEqual(obj.maxProduct(
            [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]), 1280)

    def test_7(self):
        """[0, 2] --> 2"""
        self.assertEqual(obj.maxProduct([0, 2]), 2)

    def test_8(self):
        """[-2] --> -2"""
        self.assertEqual(obj.maxProduct([-2]), -2)

    def test_9(self):
        """[2,-5,-2,-4,3] --> 24"""
        self.assertEqual(obj.maxProduct([2, -5, -2, -4, 3]), 24)


if __name__ == '__main__':
    unittest.main()

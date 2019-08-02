import unittest
from main import NumArray


class DesignTests(unittest.TestCase):

    def test_1(self):
        """sumRange works"""
        obj = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(obj.sumRange(0, 2), 1)
        self.assertEqual(obj.sumRange(2, 5), -1)
        self.assertEqual(obj.sumRange(0, 5), -3)
        self.assertEqual(obj.sumRange(2, 2), 3)


if __name__ == '__main__':
    unittest.main()

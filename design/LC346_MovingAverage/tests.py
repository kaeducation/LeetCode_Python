import unittest
from main import MovingAverage


class DesignTests(unittest.TestCase):

    def test_1(self):
        """MovingAverage Works"""
        m = MovingAverage(3)
        self.assertEqual(m.next(1), 1)
        self.assertEqual(m.next(10), 5.5)
        self.assertEqual(m.next(3), 4.666666666666667)
        self.assertEqual(m.next(5), 6)


if __name__ == '__main__':
    unittest.main()

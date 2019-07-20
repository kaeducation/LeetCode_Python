import unittest
from main import Solution

obj = Solution()


class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e


class IntervalTests(unittest.TestCase):

    def test_1(self):
        """[] --> returns 0"""
        self.assertEqual(obj.minMeetingRooms([]), 0)

    def test_2(self):
        """[[0, 30]] --> returns 1"""
        self.assertEqual(obj.minMeetingRooms([Interval(0, 30)]), 1)

    def test_3(self):
        """[[7, 10], [2, 4]] --> returns 1"""
        self.assertEqual(obj.minMeetingRooms(
            [Interval(7, 10), Interval(2, 4)]), 1)

    def test_4(self):
        """[[0, 30], [5, 10], [15, 20]] --> returns 2"""
        self.assertEqual(obj.minMeetingRooms(
            [Interval(0, 30), Interval(5, 10), Interval(15, 20)]), 2)


if __name__ == '__main__':
    unittest.main()

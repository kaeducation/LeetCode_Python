import unittest
from main import Solution

obj = Solution()


class IntervalTests(unittest.TestCase):

    def test_1(self):
        """returns true for working schedule."""
        self.assertEqual(obj.canAttendMeetings([[7, 10], [2, 4]]), True)

    def test_2(self):
        """returns true for empty schedule."""
        self.assertEqual(obj.canAttendMeetings([]), True)

    def test_3(self):
        """returns false for invalid schedule."""
        self.assertEqual(obj.canAttendMeetings(
            [[0, 30], [5, 10], [15, 20]]), False)


if __name__ == '__main__':
    unittest.main()

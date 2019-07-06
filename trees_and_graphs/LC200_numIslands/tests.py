import unittest
from main import Solution

obj = Solution()


class GraphTests(unittest.TestCase):

    def test_1(self):
        """returns 0 islands correctly."""
        self.assertEqual(obj.numIslands([
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]), 0)

    def test_2(self):
        """returns 1 island correctly."""
        self.assertEqual(obj.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]), 1)

    def test_3(self):
        """returns 3 islands correctly."""
        self.assertEqual(obj.numIslands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]), 3)


if __name__ == '__main__':
    unittest.main()

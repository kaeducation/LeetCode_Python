import unittest
from main import Solution

obj = Solution()


class MatrixTests(unittest.TestCase):

    def test_1(self):
        """returns True correctly."""
        self.assertEqual(obj.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                         "A", "D", "E", "E"]], "CESEEC"), True)
        self.assertEqual(obj.exist([["C", "A", "A"], ["A", "A", "A"], [
                         "B", "C", "D"]], "AAB"), True)

    def test_2(self):
        """returns False correctly."""
        self.assertEqual(obj.exist([["A", "B", "C", "E"],
                                    ["S", "F", "C", "S"],
                                    ["A", "D", "E", "E"]],
                                   "ABCB"), False)
        self.assertEqual(obj.exist([["a"]], "Ab"), False)


if __name__ == '__main__':
    unittest.main()

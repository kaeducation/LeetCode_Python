import unittest
from main import Solution

obj = Solution()


class HeapTests(unittest.TestCase):

    def test_1(self):
        """topKFrequent([1,1,1,2,2,3], 2) returns [1,2]"""
        self.assertEqual(
            sorted(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])

    def test_2(self):
        """topKFrequent([1], 1) returns [1]"""
        self.assertEqual(obj.topKFrequent([1], 1), [1])

    def test_3(self):
        """topKFrequent([], 10) returns []"""
        self.assertEqual(obj.topKFrequent([], 10), [])


if __name__ == '__main__':
    unittest.main()

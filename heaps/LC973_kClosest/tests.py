import unittest
from main import Solution

obj = Solution()


class HeapTests(unittest.TestCase):

    def test_1(self):
        """kClosest works"""
        res = obj.kClosest([[1, 3], [-2, 2]], 1)[0]
        res.sort()
        self.assertEqual(res, [-2, 2])

        res = obj.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
        self.assertEqual(len(res), 2)
        for sublist in res:
            sublist.sort()
        self.assertEqual([3, 3] in res, True)
        self.assertEqual([-2, 4] in res, True)


if __name__ == '__main__':
    unittest.main()

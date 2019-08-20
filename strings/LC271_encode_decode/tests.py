import unittest
from main import Solution

obj = Solution()


class StringTests(unittest.TestCase):

    def test_1(self):
        """encode returns a string"""
        self.assertEqual(
            type(obj.encode(['kevin', 'is', 'great'])) is str, True)

    def test_2(self):
        """decode returns back the correct array"""
        #          5/kevin2/is5/great
        res = obj.encode(['kevin', 'is', 'great'])
        self.assertEqual(type(res) is str, True)

        decoded_res = obj.decode(res)
        self.assertEqual(decoded_res, ['kevin', 'is', 'great'])


if __name__ == '__main__':
    unittest.main()

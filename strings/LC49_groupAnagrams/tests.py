import unittest
from main import Solution

obj = Solution()


class StringTests(unittest.TestCase):

    def test_1(self):
        """['eat', 'tea', 'tan', 'ate', 'nat', 'bat'] returns 3 groups of Anagrams"""
        res = obj.groupAnagrams(
            ["eat", "tea", "tan", "ate", "nat", "bat"])
        res.sort(reverse=True, key=len)

        for i in range(len(res)):
            sub_arr = res[i]
            sub_arr.sort()

        self.assertEqual(len(res), 3)

        sub_arr_1 = res[0]
        self.assertEqual(sub_arr_1, ["ate", "eat", "tea"])
        sub_arr_1 = res[1]
        self.assertEqual(sub_arr_1, ["nat", "tan"])
        sub_arr_1 = res[2]
        self.assertEqual(sub_arr_1, ["bat"])


if __name__ == '__main__':
    unittest.main()

import unittest
from main import RandomizedSet


class DesignTests(unittest.TestCase):

    def test_1(self):
        """insert(val) returns True for successful insertion, False for duplicate insertion"""
        random_set = RandomizedSet()
        self.assertEqual(random_set.insert(4), True)
        self.assertEqual(random_set.insert(4), False)

    def test_2(self):
        """remove(val) returns True for successful removal, False if value not present"""
        random_set = RandomizedSet()
        self.assertEqual(random_set.insert(4), True)
        self.assertEqual(random_set.remove(4), True)
        self.assertEqual(random_set.remove(4), False)

    def test_3(self):
        """getRandom() returns a random element from current set of elements"""
        random_set = RandomizedSet()
        random_set.insert(4)
        # Make sure insert() only inserts 13 once
        for i in range(0, 100):
            random_set.insert(13)

        four_count = 0
        for i in range(0, 1000):
            if random_set.getRandom() == 4:
                four_count += 1
        self.assertEqual(four_count > 400, True)
        self.assertEqual(four_count < 600, True)

        self.assertEqual(random_set.remove(4), True)
        four_count = 0
        thirteen_count = 0
        for i in range(0, 1000):
            if random_set.getRandom() == 4:
                four_count += 1
            else:
                thirteen_count += 1
        self.assertEqual(four_count, 0)
        self.assertEqual(thirteen_count, 1000)


if __name__ == '__main__':
    unittest.main()

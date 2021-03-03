import unittest
from ddt import ddt, file_data
from challenge import compareSentences

@ddt
class TestStringMatch(unittest.TestCase):

    @file_data('test_data_dict.json')
    def test_strings(self, string1, string2, expected_common, expected_difference):

        common, difference = compareSentences(string1, string2)
        self.assertCountEqual(common, expected_common)
        self.assertCountEqual(difference, expected_difference)

if __name__ == '__main__':
    unittest.main()
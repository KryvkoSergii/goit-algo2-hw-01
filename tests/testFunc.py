import unittest
from app.main import min_max_search

class TestMinMaxSearch(unittest.TestCase):
    def test_min_max(self):
        self.assertEqual(min_max_search([10, -2, 3, 14, -5]), (-5, 14))
    def test_single_value_array(self):
        self.assertEqual(min_max_search([3]), (3, 3))
    def test_empty_array(self):
        self.assertEqual(min_max_search([]), (None, None))
    def test_2_element_array(self):
        self.assertEqual(min_max_search([2,-10]), (-10, 2))

if __name__ == '__main__':
    unittest.main()
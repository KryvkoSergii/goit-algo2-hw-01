import unittest
from app.main import min_max_search, quick_select

class TestMinMaxSearch(unittest.TestCase):
    def test_min_max(self):
        self.assertEqual(min_max_search([10, -2, 3, 14, -5]), (-5, 14))
    def test_single_value_array(self):
        self.assertEqual(min_max_search([3]), (3, 3))
    def test_empty_array(self):
        self.assertEqual(min_max_search([]), (None, None))
    def test_2_element_array(self):
        self.assertEqual(min_max_search([2,-10]), (-10, 2))

class TestQuickSelect(unittest.TestCase):
    
    def test_select_duplicate(self):
        result = quick_select([10, -2, 3, 14, -5, 7, 4, 3, -1], 4)
        self.assertEqual(result, 3)
    
    def test_select_single(self):
        result = quick_select([10, -2, 3, 14, -5, 7, 4, 3, -1], 6)
        self.assertEqual(result, 4)
    
    def test_select_min(self):
        result = quick_select([10, -2, 3, 14, -5, 7, 4, 3, -1], 1)
        self.assertEqual(result, -5)
    
    def test_select_max(self):
        result = quick_select([10, -2, 3, 14, -5, 7, 4, 3, -1], 9)
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()
"""
Unit Tests for Health Record Symmetry Checker
"""

import unittest
from health_record import (
    ListNode, 
    isHealthRecordSymmetric, 
    create_linked_list
)


class TestHealthRecordSymmetric(unittest.TestCase):
    """Test suite for isHealthRecordSymmetric function."""
    
    # ==================== NORMAL CASES ====================
    
    def test_normal_odd_length_palindrome(self):
        """Odd-length symmetric record: [120, 80, 75, 80, 120]"""
        head = create_linked_list([120, 80, 75, 80, 120])
        self.assertTrue(isHealthRecordSymmetric(head))
    
    def test_normal_even_length_palindrome(self):
        """Even-length symmetric record: [98, 102, 102, 98]"""
        head = create_linked_list([98, 102, 102, 98])
        self.assertTrue(isHealthRecordSymmetric(head))
    
    def test_normal_not_palindrome(self):
        """Non-symmetric record: [120, 80, 75, 90, 120]"""
        head = create_linked_list([120, 80, 75, 90, 120])
        self.assertFalse(isHealthRecordSymmetric(head))
    
    def test_normal_three_elements_symmetric(self):
        """Three element symmetric: [98, 102, 98]"""
        head = create_linked_list([98, 102, 98])
        self.assertTrue(isHealthRecordSymmetric(head))
    
    def test_normal_three_elements_not_symmetric(self):
        """Three element non-symmetric: [98, 102, 99]"""
        head = create_linked_list([98, 102, 99])
        self.assertFalse(isHealthRecordSymmetric(head))
    
    # ==================== EDGE CASES ====================
    
    def test_edge_empty_list(self):
        """Empty list is symmetric."""
        self.assertTrue(isHealthRecordSymmetric(None))
    
    def test_edge_single_element(self):
        """Single element is symmetric."""
        head = create_linked_list([100])
        self.assertTrue(isHealthRecordSymmetric(head))
    
    def test_edge_two_elements_same(self):
        """Two identical elements: [85, 85]"""
        head = create_linked_list([85, 85])
        self.assertTrue(isHealthRecordSymmetric(head))
    
    def test_edge_two_elements_different(self):
        """Two different elements: [85, 90]"""
        head = create_linked_list([85, 90])
        self.assertFalse(isHealthRecordSymmetric(head))
    
    def test_edge_all_same_values(self):
        """All same values: [72, 72, 72, 72]"""
        head = create_linked_list([72, 72, 72, 72])
        self.assertTrue(isHealthRecordSymmetric(head))
    
    def test_edge_long_palindrome(self):
        """Long symmetric record."""
        values = [60, 70, 80, 90, 100, 90, 80, 70, 60]
        head = create_linked_list(values)
        self.assertTrue(isHealthRecordSymmetric(head))


def run_tests_with_verbosity(verbosity=2):
    """Run all tests with specified verbosity level."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestHealthRecordSymmetric))
    runner = unittest.TextTestRunner(verbosity=verbosity)
    runner.run(suite)


if __name__ == '__main__':
    run_tests_with_verbosity(verbosity=2)
import unittest

from utils import minimum


class TestMinimum(unittest.TestCase):
    def test_single_value(self):
        self.assertEqual(minimum(5), 5)

    def test_order_values(self):
        self.assertEqual(minimum(5, 8), 5)

    def test_non_order_values(self):
        self.assertEqual(minimum(5, 8, 2, 3), 2)

    def test_have_negative_values(self):
        self.assertEqual(minimum(5, -8, 2, 3), -8)

    def test_have_zero_values(self):
        self.assertEqual(minimum(5, 0, 2, 3), 0)

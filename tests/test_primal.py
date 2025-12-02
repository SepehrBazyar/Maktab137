import unittest

from utils import is_primal


class TestPrimal(unittest.TestCase):
    def test_true_is_primal(self):
        self.assertTrue(is_primal(5))

    def test_false_is_primal(self):
        self.assertFalse(is_primal(8))

    def test_one_is_primal(self):
        self.assertFalse(is_primal(1))

    def test_negative_is_primal(self):
        with self.assertRaises(ValueError):
            is_primal(-2)


# unittest.main()

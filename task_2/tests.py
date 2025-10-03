import unittest
from sol import *


class Test(unittest.TestCase):
    # Тест функции перебора
    def test_incr1(self):
        self.assertEqual(incr_guess_number(4, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [4, 3])

    def test_incr2(self):
        self.assertEqual(incr_guess_number(12, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [12, 8])

    def test_incr3(self):
        self.assertEqual(incr_guess_number(1, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [1, 1])

    def test_incr4(self):
        self.assertEqual(incr_guess_number(63, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [63, 13])

    def test_incr5(self):
        self.assertEqual(incr_guess_number(5, [5]), [5, 1])

    def test_incr6(self):
        self.assertEqual(incr_guess_number(4, [1, 2, 5, 6]), [-1, -1])

    def test_incr7(self):
        self.assertEqual(incr_guess_number(2, []), [-1, -1])

    # Тест функции бинарного поиска
    def test_bin1(self):
        self.assertEqual(bin_guess_number(4, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [4, 4])

    def test_bin2(self):
        self.assertEqual(bin_guess_number(12, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [12, 3])

    def test_bin3(self):
        self.assertEqual(bin_guess_number(1, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [1, 4])

    def test_bin4(self):
        self.assertEqual(bin_guess_number(63, [1, 2, 4, 6, 7, 8, 10, 12, 15, 32, 40, 56, 63]), [63, 4])

    def test_bin5(self):
        self.assertEqual(bin_guess_number(5, [5]), [5, 1])

    def test_bin6(self):
        self.assertEqual(bin_guess_number(4, [1, 2, 5, 6]), [-1, -1])

    def test_bin7(self):
        self.assertEqual(bin_guess_number(2, []), [-1, -1])


if __name__ == '__main__':
    unittest.main()

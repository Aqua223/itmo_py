import unittest
from sol import gen_bin_tree


class Test(unittest.TestCase):
    # Тест соответствия бинарного дерева
    def test_gen_bin_tree1(self):
        self.assertEqual(gen_bin_tree(1, 1), {1: []})

    def test_gen_bin_tree2(self):
        self.assertEqual(gen_bin_tree(1, 2), {1: [{3: []}, {5: []}]})

    def test_gen_bin_tree3(self):
        self.assertEqual(gen_bin_tree(0, 2), {0: [{0: []}, {4: []}]})

    def test_gen_bin_tree4(self):
        self.assertEqual(gen_bin_tree(7, 3), {7: [{21: [{63: []}, {25: []}]}, {11: [{33: []}, {15: []}]}]})

    def test_gen_bin_tree5(self):
        self.assertEqual(gen_bin_tree(5, 3), {5: [{15: [{45: []}, {19: []}]}, {9: [{27: []}, {13: []}]}]})

    def test_gen_bin_tree6(self):
        self.assertEqual(gen_bin_tree(-5, 2), {-5: [{-15: []}, {-1: []}]})

    def test_gen_bin_tree7(self):
        self.assertEqual(gen_bin_tree(-5, 1), {-5: []})


if __name__ == '__main__':
    unittest.main()
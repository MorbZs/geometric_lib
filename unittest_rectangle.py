import unittest
from rectangle import*


class RectangleTestCase(unittest.TestCase):
    def test_normal_area(self):
        result = area(4, 3)
        self.assertEqual(result, 12)

    def test_sec_zero_area(self):
        result = area(4, 0)
        self.assertEqual(result, 0)

    def test_fst_zero_area(self):
        result = area(0, 3)
        self.assertEqual(result, 0)

    def test_fst_wrong_type_area(self):
        result = area("4", 3)
        self.assertEqual(result, 12)

    def test_sec_wrong_type_area(self):
        result = area(4, "3")
        self.assertEqual(result, 12)

    def test_normal_perimeter(self):
        result = perimeter(4, 3)
        self.assertEqual(result, 14)

    def test_sec_zero_perimeter(self):
        result = perimeter(4, 0)
        self.assertEqual(result, 0)

    def test_fst_zero_perimeter(self):
        result = perimeter(0, 3)
        self.assertEqual(result, 0)

    def test_fst_wrong_type_perimeter(self):
        result = perimeter("4", 3)
        self.assertEqual(result, 12)

    def test_sec_wrong_type_perimeter(self):
        result = perimeter(4, "3")
        self.assertEqual(result, 12)

    def test_minus_area(self):
        result = area(-5, 6)
        self.assertEqual(result, 0)

    def test_minus_perimeter(self):
        result = perimeter(-5, 6)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
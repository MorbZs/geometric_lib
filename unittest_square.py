import unittest
from square import*


class SquareTestCase(unittest.TestCase):
    def test_normal_area(self):
        result = area(5)
        self.assertEqual(result, 25)

    def test_zero_area(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_wrong_type_area(self):
        result = area("5")
        self.assertEqual(result, 25)

    def test_normal_perimeter(self):
        result = perimeter(5)
        self.assertEqual(result, 20)

    def test_zero_perimeter(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_wrong_type_perimeter(self):
        result = perimeter("5")
        self.assertEqual(result, 25)

    def test_minus_area(self):
        result = area(-5)
        self.assertEqual(result, 0)

    def test_minus_perimeter(self):
        result = perimeter(-5)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

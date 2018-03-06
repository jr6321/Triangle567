"""  Test cases for Triangles """


import unittest
from triangles import check_args, classify_triangle

class TestTriangles(unittest.TestCase):
    """ test triangles """
    def test_invalid_inputs(self):
        self.assertRaises(ValueError, check_args, [0])
        self.assertRaises(ValueError, check_args, ['string'])
        self.assertRaises(ValueError, check_args, [1, 1, 3])

    def test_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')
        self.assertEqual(classify_triangle(1.5, 1.5, 1.5), 'equilateral')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'equilateral')

    def test_isoscoles(self):
        self.assertEqual(classify_triangle(3, 3, 2), 'isoscoles')
        self.assertEqual(classify_triangle(1.5, 1.5, 1.5), 'equilateral')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'equilateral')


if __name__ == "__main__":
    unittest.main(exit=False)
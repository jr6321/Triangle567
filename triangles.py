""" 
    SSW 567 clasify Triangles with test suite and code coverage
"""
import unittest

def check_args(args):
    """ given a list of sorted args, verify that all are numbers > 0 and a + b >= c """
    for arg in args:
        if (not (isinstance(arg, int) or isinstance(arg, float))) or arg <= 0:
            raise ValueError("arguments must be numbers > 0: {} is invalid".format(arg))

    if args[0] + args[1] < args[2]:
        raise ValueError("Invalid Triangle: sum any two sides < third side")

    return True  # the arguments look okay

def is_right(args):
    """ args is a sorted list of numbers.   return True if a^2 + b^2 == c^2 """
    return round((args[0] ** 2 + args[1] ** 2), 2) == round(args[2] ** 2, 2)

def classify_triangle(a, b, c):
    """ identify equilateral, isosceles, and scalene triangles plus identify if right triangle 
        Return one of 'equilateral', 'isosceles', 'scalene', 'isosceles right', 'scalene right', 'NotATriangle'

        Sort the arguments to simplify processing on order insignificance.
    """
    # first test that the arguments are valid.  All args must be numbers and > 0
    
    args = sorted([a, b, c])
    try: 
        check_args(args)
    except ValueError as e:
        print(e)
        return 'NotATriangle'
    else:
        ret = "scalene"

        if args[0] == args[1] and args[2] == args[2]:
            ret = 'equilateral'
        elif args[0] == args[1] or args[1] == args[2]:
            ret = "isoscoles"

        if is_right(args):
            ret += " right"

        return ret
            

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

    ef test_isoscoles(self):
        self.assertEqual(classify_triangle(3, 3, 2), 'isoscoles')
        self.assertEqual(classify_triangle(1.5, 1.5, 1.5), 'equilateral')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'equilateral')


if __name__ == "__main__":
    unittest.main(exit=False)
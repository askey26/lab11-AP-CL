import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(4, 5), 9)
        self.assertNotEqual(add(9, 10), 21)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 4), 1)
        self.assertEqual(sub(4, 30), -26)
        self.assertNotEqual(sub(10, 1), -4)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 10), 1)
        self.assertEqual(log(11, ))

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
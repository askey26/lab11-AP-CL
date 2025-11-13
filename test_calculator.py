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
    def test_multiply(self): # 3 assertions
        self.assertTrue(mul(3, 4) , 12)
        self.assertTrue(mul(1, 2) ,  2)
        self.assertTrue(mul(-5, 3) ,-15)

    def test_divide(self): # 3 assertions
        self.assertTrue(div(6, 2) , 3)
        self.assertTrue(div(10, 5) , 2)
        self.assertTrue(div(15, 3) , 5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 10), 1)
        self.assertEqual(log(100, 10), 2)
        self.assertEqual(log(16, 2), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-3, -4)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertTrue(hypotenuse(3, 4) , 5)
        self.assertTrue(hypotenuse(5, 12) , 13)
        self.assertTrue(hypotenuse(8, 15) , 17)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertTrue(square_root(4), 2)
        self.assertTrue(square_root(9), 3)
        self.assertTrue(square_root(16) , 4)
        with self.assertRaises(ValueError):
            square_root(-16)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
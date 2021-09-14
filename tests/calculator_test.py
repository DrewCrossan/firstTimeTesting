# tests/calculator_test.py

import unittest
from src.calculator import * #add, divide, exponent2, multiply, subtract, exponent2, exponent3, exponent4, square_root, volume

class TestCalculator(unittest.TestCase): # NEW
    def test_add(self): # NEW
        self.assertEqual(5, add(2, 3))
    
    def test_subtract(self): # NEW
        self.assertEqual(2, subtract(5, 3))

    def test_divide(self): # NEW
        self.assertEqual(3, divide(9, 3))
    
    def test_multiply(self): # NEW
        self.assertEqual(18, multiply(6, 3))
    
    def test_exponent(self): # NEW
        self.assertEqual(9, exponent2(3))
    
    def test_exponent3(self): # NEW
        self.assertEqual(27, exponent3(3))

    def test_exponent4(self): # NEW
        self.assertEqual(81, exponent4(3))

    def test_square_root(self):
        self.assertEqual(3, square_root(9))
    
    def test_volume(self):
        self.assertEqual(162, volume(3, 6, 9))

    def test_is_circle_round(self):
        self.assertEqual(3.14, round(is_circle_round(22, 7), 2))






    
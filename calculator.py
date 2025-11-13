# https://github.com/askey26/lab11-AP-CL
# Partner 1: Askey Pierre
# Partner 2: Cody Lu
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example


import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b

def hypotenuse(a, b):
    return math.hypot(a, b)
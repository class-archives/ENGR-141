# Activity: Python 1 Post Activity
# File: Py1_PA_Task1_katherto.py
# Date: September 17, 2015
# By: Kathryn Atherton
# katherto
# Section: 4
# Team: 59
#
# ELECTRONIC SIGNATURE
# Kathryn Atherton
# The electronic signature above indicates that the program 
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# This program demonstrates the equivalence between doing 
# calculations with decimal numbers and doing the same
# calculations with fractions. It generates two random 
# numbers, rounds them to the nearest tenth, adds them
# together, converts the numbers to fractions, and adds 
# them together.

from random import uniform
from fractions import Fraction

a = uniform(0,10)
b = uniform(0,10)

c = round(a,1)
d = round(b,1)

decimal = c + d

e = Fraction(c)
f = Fraction(d)

fraction = e + f

print('First Random Number:', a)
print('Second Random Number:', b)

print(c, '+', d, '=', decimal)
print(e, '+', f, '=', fraction)
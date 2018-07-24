# Activity: Python 2 Post Activity
# File: Py2_PA_Task2_Main_katherto.py
# Date: September 27, 2015
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
# PROGRAM DESCRIPTION
# This program can be used in the main 
# program to find the pressure of a non-ideal gas, and, if the 
# resulting pressure is not within the desired range,
# the program will find the minimum required temperature 
# adjustment in order to return the pressure to the desired range.

import math
from Py2_PA_Task2_Functions_katherto.py import pressure, highP_tempchange, lowP_tempchange

R = 0.0821 #L * atm / mol * K
V = 18 # L/mol
T = float(input('Input Initial Temperature in Kelvin:\n'))
a = 6.49 # L^2 atm / mol^2
b = 0.0562 # L / mol

pressure(R, T, V, a, b)

if 1.1 <= P <= 1.2:
    print('Initial conditions:\n')
    print('Volume =', V, 'L/mol')
    print('Initial temperature =', T, 'K')
    print('Parameter a =', a, 'L^2 atm / mol^2')
    print('Parameter b =', b, 'L /mol')
    print('Resulting pressure =', P, 'atm')
    print('No temperature change needed.')

elif P < 1.1:
    lowP_tempchange(R, V, a, b)
    print('Initial conditions:\n')
    print('Volume =', V, 'L/mol')
    print('Initial temperature =', T, 'K')
    print('Parameter a =', a, 'L^2 atm / mol^2')
    print('Parameter b =', b, 'L /mol')
    print('Resulting pressure =', P, 'atm')
    print('Required temperature increment for in-range pressure =', delta_T, 'K')
    print('New temperature =', new_T, 'K')
    print('New pressure = 1.1 atm')

else:
    highP_tempchange(R, V, a, b)
    print('Initial conditions:\n')
    print('Volume =', V, 'L/mol')
    print('Initial temperature =', T, 'K')
    print('Parameter a =', a, 'L^2 atm / mol^2')
    print('Parameter b =', b, 'L /mol')
    print('Resulting pressure =', P, 'atm')
    print('Required temperature increment for in-range pressure =', delta_T, 'K')
    print('New temperature =', new_T, 'K')
    print('New pressure = 1.2 atm')



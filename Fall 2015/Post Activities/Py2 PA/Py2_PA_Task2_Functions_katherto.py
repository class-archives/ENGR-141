# Activity: Python 2 Post Activity
# File: Py2_PA_Task2_functions_katherto.py
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
# This program creates the functions that can be used in the main 
# program to find the pressure of a non-ideal gas, and, if the 
# resulting pressure is not within the desired range,
# the second function will find the minimum required temperature 
# adjustment in order to return the pressure to the desired range.

import math 

def pressure(R, T, V, a, b):
    P = ((R * T) / (V - b)) - (a / (V ** 2))

def highP_tempchange(R, V, a, b):
    new_T = (1.2 + (a / (V ** 2)) * ((V - b) / R)
    delta_T = new_T - T

def lowP_tempchange(R, V, a, b):
    new_T = (1.1 + (a / (V ** 2)) * ((V - b) / R)
    delta_T = new_T - T


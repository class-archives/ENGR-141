# Activity: Python 1 Post Activity
# File: Py1_PA_Task2_katherto.py
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
# This program can be used to calculate the equivalent
# resistance of series and parallel configurations of 2 
# resistors. The output is formatted as a table.  

from tabulate import tabulate
import math

First_Resistance = round(float(input("Enter First Resistance:")), 1)
Second_Resistance = round(math.sqrt(5.6) * math.pi, 1)

Parallel = round(((1 / First_Resistance) + (1 / Second_Resistance)) ** (-1), 1)
Series = round(First_Resistance + Second_Resistance, 1)

table = [['Type of Resistance', 'First Resistance', 'Second Resistance', 'Equivalent Resistance'], ['Parallel', First_Resistance, Second_Resistance, Parallel], ['Series', First_Resistance, Second_Resistance, Series]]
print tabulate(table)
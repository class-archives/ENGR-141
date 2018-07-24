# Activity: Python 1 ACT/Bonus-- Task 5
# File: Py1_ACT_Task5_Team59.py
# Date: 22 September 2015
# By: Kathryn Atherton
# katherto
# Ryan Hellyer
# rhellyer
# Natalie Zimmermann
# nzimmermn
# Section: 04, 3:30, SHRV C111
# Team: 59 
# 
# ELECTRONIC SIGNATURE
# Kathryn Atherton
# Ryan Hellyer
# Natalie Zimmermann
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an 
# equal participant in its creation. In addition, each
# member of the team has a general understanding of 
# all aspects of the program development and execution.
# 
# This program can be used to compute the area of a 
# circle and then display the result. It includes comments 
# explaining acceptable inputs as well as the steps. 

import math #imports the math functions 

r = float(input("Enter radius value:/n") #allows user to input the value for the radius
#Changes input type to float so that math calculations can be done with the input.
#Acceptable inputs would be any number that represents the radius of the given circle.
units = input("Enter units of radius value:/n") #allows user to define the units used in the calculation

area = math.pi * (r ** 2) #computes the area of the circle and creates variable for value

print("The area of a circle with a radius of", r, "[", units, "] is", area, "[", units, "^2].") 
#prints the area and displays the initial value of r as well as the initial units and final units of the respective values.

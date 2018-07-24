# Activity: Python 1 ACT/Bonus--Task 1
# File: Py1_ACT_Task1_Team59.py
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
# triangle, which has two sides of 12 cm and 4 cm and 
# an angle of 30 degrees in between and then output the 
# result in a sentence.

import math

#Knowns
x = 12 #cm
y = 4 #cm
z = 30 #degrees

#Convert z to radians
angle = (z * math.pi) / 180 #radians

#Compute Area
area = (1 / 2) * x * y * math.sin(angle) #cm^2

#Print Statement
print("The area of a traingle is", area, "[cm^2] for a given length of", x, "[cm]")
print("and", y, "[cm] with the angle of", z, "[degrees] in between.")
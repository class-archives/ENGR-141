# Activity: Py2 CFU
# File: Py2_CFU_katherto.py
# Date: 23 September 2015
# By: Kathryn Atherton
# katherto
# Section: 04
# Team: 59 
#
# ELECTRONIC SIGNATURE
# Kathryn Atherton
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# This program can be used to receive an input of the distance
# a ball lands from the center of a circle (in the x and y 
# directions) and then compute the total distance from the center
# of the circle, find the color of the zone the ball landed in,
# and tell how many points were earned by landing the ball in 
# that zone. 

import math

x = float(input("Enter distance from center in x direction:\n"))
y = float(input("Enter distance from center in y direction:\n"))

def distTarget(x,y):
    math.sqrt((x ** 2) + (y ** 2))

r = distTarget(x,y)

def points(r):
    if (0 <= r <= 4):
        return 10
    elif (4 < r <= 8):
        return 8
    elif (8 < r <= 12):
        return 6
    else:
        return 0

points = points(r)

if (points == 10):
    color = 'yellow'
elif (points == 8):
    color = 'red'
elif (points == 6):
    color = 'blue'
else:
    color = 'none'

if color == 'none':
    print('The ball did not land on the target. Zero points were made.')
else:
    print('Ball landed in the', color, 'zone for' points, 'points.')
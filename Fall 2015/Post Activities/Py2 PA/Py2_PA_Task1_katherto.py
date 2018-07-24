# Activity: Python 2 Post Activity
# File: Py2_PA_Task1_katherto.py
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
# This program can be used to determine if there is refraction
# or total internal reflection when light passes through two 
# optical media, given n1, n2, and the angle at which the light
# encounters the second medium. When light is refracted, the 
# program can also determine the second angle, the ending 
# distance of the ray of light, and the critical angle.

import math

def theta_2(x,y,z):
    (math.asin((x / y) * math.sin(z)) * 180) / math.pi

def d3(x,a,y,b):
    (x * math.tan(a)) + (y * math.tan(b))

def theta_c(x,y):
    (math.asin(y / x) * 180) / math.pi

n1 = float(input('Enter the index of refraction of medium 1:\n'))
n2 = float(input('Enter the index of refraction of medium 2:\n'))

theta = float(input('Input incoming angle in degrees:\n'))
theta_1 = (theta * math.pi) / 180

if n1 > n2:
    print('There is total internal reflection. The angle of reflection is', theta, 'degrees.')

elif n2 > n1:
    print('There is refraction with a leaving angle of', theta_2(n1,n2,theta_1), 'degrees.')
    d1 = float(input('Enter the distance the light travels through medium 1 in cm:\n'))
    d2 = float(input('Enter the distance the light travels through medium 2 in cm:\n'))
    print('The ending distance for the light ray is', d3(d1,theta_1,d2,theta_2), 'cm.')
    print('For these two media, the critical angle is', theta_c(n1,n2), 'degrees.') 

else:
    print('There is no change in the path of the light, as the indecies of refraction are the same.')


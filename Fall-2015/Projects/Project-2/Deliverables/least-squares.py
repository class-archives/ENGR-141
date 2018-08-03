# Activity: Project 2: Least Squares Program
# File: Proj2_LeastSquares_Team59.py
# Date: October 28, 2015
# By: Kathryn Atherton
# katherto
# Ryan Hellyer
# rhellyer
# Natalie Zimmermann
# zimmermn
# Section: 4
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
# Description of Program
#

import math

data = open('Proj2_Input_PrintSpeed.csv')
data_list = data.readlines()
data.close()

#create lists of dimensional error and print speed values
dim_errors = []
print_speeds = []

for line in data_list:
	#create list of the individual data points from the current line
	line_values = line.split(',')
	
	#add relevant values to their respective lists
	print_speeds.append(line_values[0])
	dim_errors.append(line_values[2])
	
def linear_origin(x,y):
	numerator = 0
	denominator = 0
	counter = 0
	while counter < len(x):
		numerator += float(x[counter]) * float(y[counter])
		denominator += float(x[counter]) ** 2
		counter += 1
	return numerator/denominator
	
a1 = linear_origin(print_speeds,dim_errors)

print('The linear regression line is y = %0.5f * x.' % a1)


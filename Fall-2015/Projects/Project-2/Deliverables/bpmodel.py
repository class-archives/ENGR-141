# Activity: Project 2: Model
# File: Proj2_BPModel_Team59.py
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
# DESCRIPTION OF PROGRAM 
# This program takes the user inputs of part volume, tolerance,
# and a Factor of Safety, as well as experimental data from 
# print speed error testing to find the relationship between
# print speed and dimensional error, and then outputs the
# optimal printer head speed, print aperture, and culture
# temperature, as well as the production time, the dimensional 
# error, and the final cost, as well as the cost due to the 
# Factor of Safety for the printing of a certain part, as defined 
# by the user.

# importing module
import math

# user inputs
volume = float(input('Please input the volume of the desired part in cm^3:'))
tolerance = float(input('Please input the part tolerances in mm:'))
fos = float(input('Please input the factor of safety for the ' 
'part as a percentage:'))

# loop to be sure that FoS is valid
while fos < 100:
	fos = float(input('Please input a new factor of safety for the part ' 
	'as a percentage that is greater than 100%:'))

# converting fos to decimal
fos = fos / 100 

# converting volume to cubic millimeters
volume = volume * 1000 

# find the estimated dimensional error given FoS and tolerance 
dimerror = tolerance / fos

# finding linear regression
# importing data
data = open('Proj2_Input_PrintSpeed.csv')
data_list = data.readlines()
data.close()

# create lists of dimensional error and print speed values
dim_errors = []
print_speeds = []

# sorting through data
for line in data_list:
	# create list of the individual data points from the current line
	line_values = line.split(',')
	
	# add relevant values to their respective lists
	print_speeds.append(line_values[0])
	dim_errors.append(line_values[2])

# create the function to find the a1 coefficient	
def linear_origin(x,y):
	numerator = 0
	denominator = 0
	counter = 0
	while counter < len(x):
		numerator += float(x[counter]) * float(y[counter])
		denominator += float(x[counter]) ** 2
		counter += 1
	return numerator/denominator

# run the function	
a1 = linear_origin(print_speeds,dim_errors)

# find the values for head speed, aperture, and temperature 
# using the regressions found with respect to FoS
head_speed = (dimerror) / a1
aperture = (math.log(dimerror / 0.0054)) / 2.9094
temperature = (dimerror / 0.00002) ** (1 / 3.2563)

# find the values for head speed, aperture, and temperature 
# using the regressions found with respect to original tolerance
head_speed_tol = (tolerance) / a1
aperture_tol = (math.log(tolerance / 0.0054)) / 2.9094
temperature_tol = (tolerance / 0.00002) ** (1 / 3.2563)

# find the actual printing time and cure time
printing_time = volume / (head_speed * aperture)
cure_time = (1570 / (temperature)) + 20

# find the printing and cure times without FoS taken into account
printing_time_tol = volume / (head_speed_tol * aperture_tol)
cure_time_tol = (1570 / (temperature_tol)) + 20

# find the actual production time
if printing_time >= cure_time:
	production_time = printing_time + 20
else:
	production_time = cure_time

# find the production time without taking FoS into account
if printing_time_tol >= cure_time_tol:
	production_time_tol = printing_time_tol + 20
else: 
	production_time_tol = cure_time_tol

#find the cost with and without respect to FoS
cost = (18 * production_time) + (volume * 0.5)
cost_tol = (18 * production_time_tol) + (volume * 0.5)

#find the cost that FoS adds
added_cost = cost - cost_tol

#print statements
print('The optimal head speed for the desired part in mm/min '
'is %0.5f.' % head_speed)
print('The optimal print aperture for the desired part in mm^2 '
'is %0.5f.' % aperture)
print('The optimal culture temperature for the desired part in '
'degrees Celsius is %0.5f.' % temperature)
print('The production time for the desired part in minutes '
'is %d.' % production_time)
print('The estimated dimensional error for the desired part in '
'mm is %0.5f.' % dimerror)
print('The added cost due to the factor of safety for the desired part'
' is $ %0.2f.' % added_cost)
print('The total cost for the desired part is $ %0.2f.' % cost)
# Activity: Python 2 ACT/Bonus
# File: Py2_ACT_Task2_team59.py
# Date: September 23, 2015
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
# This function can be used to determine the state of a boiler
# given the inputs of temperature and pressure based on 
# dangerous and normal parameters. 

T = int(input("Enter Temperature in degrees Celsius:\n"))
P = int(input("Enter Pressure in MPa:\n"))

if ((T > 1000) or (P > 20)):
	print("Danger")
	if (T > 1000):
		print("High Temperature")
	else:
		print("High Pressure")
elif ((750 < T < 1000) and (10 < P < 20)):
	print("Normal")
else:
	print("Warning")
	if (T < 750):
		print("Low Temperature")
	else:
		print("Low Pressure")
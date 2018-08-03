#Activity no. : Python 2 Activity

#File: Py2_ACT_Task3_katherto.py

#By: Natalie Zimmermann

#login: zimmermn

#By:Ryan Hellyer

#login:rhellyer

#By: Kathryn Atherton

#login: katherto

#Section: 04

#Team: Team 59

#
#ELECTRONIC SIGNATURE

#Natalie Zimmermann

#Ryan Hellyer

#Kathryn Atherton

#
#The electronic signature above indicates the program submitted for evaluation represents the work of all team  members and that all team  

#members have a general understanding of the program. 

#
#PROGRAM DESCRIPTION

#The following program has two user-defined functions, distanceRover that calculates 

#the distance a robot can drive in a given time, and solarPanelArea, that calculates

#the area needed for a specific efficency, power, and solar irradiance


speed = 1

time = 2

power = 100

efficency = 0.25

area = 0

distance = 0

solar_Irradiance = 590
 


time = time * 60 * 60
 


def distanceRover (speed, time, distance):
	
    distance = speed * time 
	
    return distance 



def solarPanelArea (power, efficency, area, distance, solar_Irradiance):
	
    area = power / (efficency * solar_Irradiance) 
	
    return area

print ('The robot travelled', distanceRover (speed, time, distance),' cm in', time, 
'seconds\nAnd the solar panel surface area is:',solarPanelArea (power, efficency, area, distance, solar_Irradiance),
'square meters')
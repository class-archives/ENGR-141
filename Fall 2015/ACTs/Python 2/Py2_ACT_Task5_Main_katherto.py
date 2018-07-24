#Activity no. : Python 2 Activity

#File: Py2_ACT_Task5_Main_katherto.py

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

#This program calculates the number of real roots of a quadratic function, knowing the discriminant
.


a = 0

b = 0

c = 0

dis = 0

no_real = ''

one_real = ''

two_real = ''



from Py2_ACT_Task5_Main_zimmermn import discriminant


a = int(input('Please input a value a: '))

b = int(input('Please input a value b: '))

c = int(input('Please input a value c: '))



dis = discriminant (a, b, c)


if dis < 0:
	
     no_real = 'True'
	
     one_real = 'False'
	
     two_real = 'False'
	


elif dis == 0:
	
     no_real = 'False'
	
     one_real = 'True'
	
     two_real = 'False'
	

else:
	
     no_real = 'False'
	
     one_real = 'False'
	
     two_real = 'True'
 
 


print ('The inputs are:\na=',a , 'b =', b, 'c =', c)

print ('No real roots : ', no_real)

print ('One real root : ', one_real)

print ('Two real roots : ', two_real)
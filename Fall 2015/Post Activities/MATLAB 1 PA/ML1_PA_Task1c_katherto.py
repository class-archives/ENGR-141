# Activity: MATLAB 1 Post Activity
# File: katherto.py
# Date: 16 November 2015
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
# A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES 
# This function contains the function getIBeam. It takes in
# the inputs of height, width, and thickness and outputs the
# height, width, thickness, and cross-sectional area of the
# I-beam. 

# define function
def getIBeam(h, w, t):
	a = ((w * t) * 2) + ((h - (2 * t)) * t)
	return a
	
# receive inputs from user
inputs = input('Please input the height, width, and thickness '
'of the I-beam in feet, separated by commas:')

# make a list out of inputs
list = inputs.split(',')

#tell user that program is running
print('... running')

# defining variables
h = float(list[0])
w = float(list[1])
t = float(list[2])

# call function
a = getIBeam(h, w, t)

# receive file name from user to print results to
filename = input('Please input the file name to write the results to:')


# write to file
output = open(filename, 'w')
output.write('For a beam with a height of %.1f ft, width of %.2f ft, and a'
' thickness of %.3f ft, the cross-sectional area is %.2f sq. ft.' % (h, w, t, a))
output.close()

#tell user that file has been written
print('... output written to file ' filename)
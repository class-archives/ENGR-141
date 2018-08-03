# Activity: Python 4 Post Activity
# File: Py4_PA_Task1_katherto.py
# Date: October 10, 2015
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
# PROGRAM DESCRIPTION
# This program prompts the user for an input file name, an 
# output file name, then creates a new file with the given
# output file name, writing the file so that each line of 
# the input file is written into it with step numbers 
# appended to the beginning of each line.

old_file = input('Enter the filename of the input file:')
new_file = input('Enter the filename of the output file:')

f = open(old_file)
contents = f.readlines()
f.close()

f_new = open(new_file, 'a')

l = 1

for line in contents:
	l = str(l)
	f_new.write('Step %s:' % l)
	f_new.write(line)
	l = int(l)
	l = l + 1

f_new.close()
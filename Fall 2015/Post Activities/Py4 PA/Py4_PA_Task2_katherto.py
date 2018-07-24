# Activity: Python 4 Post Activity
# File: Py4_PA_Task2_katherto.py
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
# This program will prompt the user to search for a word in 
# an input file. The program will search the input file for
# the search word and compute the percentage of times the word
# appears in the text. 

word = input('Enter the search word:')
word = word.lower()
word = ' ' + word + ' '

file = open('Text_File.txt')
contents = file.read()
contents = contents.lower()
contents = contents.replace('!',' ')
contents = contents.replace('@',' ')
contents = contents.replace('#',' ')
contents = contents.replace('$',' ')
contents = contents.replace('%',' ')
contents = contents.replace('^',' ')
contents = contents.replace('&',' ')
contents = contents.replace('*',' ')
contents = contents.replace('(',' ')
contents = contents.replace(')',' ')
contents = contents.replace('_',' ')
contents = contents.replace('-',' ')
contents = contents.replace('+',' ')
contents = contents.replace('=',' ')
contents = contents.replace('{',' ')
contents = contents.replace('}',' ')
contents = contents.replace('[',' ')
contents = contents.replace(']',' ')
contents = contents.replace('|',' ')
contents = contents.replace(':',' ')
contents = contents.replace(';',' ')
contents = contents.replace('"',' ')
contents = contents.replace("'",'apostrophe')
contents = contents.replace('<',' ')
contents = contents.replace('>',' ')
contents = contents.replace(',',' ')
contents = contents.replace('.',' ')
contents = contents.replace('?',' ')
contents = contents.replace('/',' ')

file.close()

num_words = 0
search = 0

for line in contents:
	words = line.split()
	num_words = num_words + len(words)

search = contents.find(word)
if search < 0:
	search = 0
		
percent_word = (search / num_words) * 100

print('The search word occurred %f%% of the time.' % percent_word)
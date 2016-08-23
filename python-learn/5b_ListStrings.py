#!/usr/bin/python
 
# billiescodes 2016
# 5b_ListStrings_fast.py
# Ex. 5 List overlap v.2.0  Strings
# Same as exercise 5 with numeric list, but generate random lists of strings from a text
# use alice.txt to draw random Alice in Wonderland

import sys
import random

def listgen(filename,length):
	# NOTE
	# 1.open file -- go through lines -- go through words in line
	# 2. store words in ARRAY 
	# 3. generate a random number from len(ARRAY) -- use as index to generate random list of strings 

	input_file = open(filename, 'r')   # #open file
	words = []

	# loop through all the lines; 'line' is a single string
	for line in input_file:
		a = 0
		# split method returns the words from the string 'line' 
		tmp_words = line.split()	
		for a in range(len(tmp_words)):
			words.append(tmp_words[a]) 

	stringlist = [words[random.randrange(0,len(words))] for i in range(length) ]
	return stringlist 

def compare(list1,list2):
	tmp=[]
	for var in list1:
		if var in list2:
			if var not in tmp:	# this will get rid of duplicates  
				tmp.append(var)
	return tmp


def main(): 
	
	test = True
	if len(sys.argv) !=2: 
		print 'usage is /.5b_ListOverlap_strings.py <file>'
		sys.exit(1)

	print "\n \t\t\t ~ List overlap with Strings~ \n "

	filename = sys.argv[1]
	print "generate a random list of strings from:", filename
	strings1 = listgen(filename, 15)
	strings2 = listgen(filename,15) 		
	print "\n the generated list of words are: "
	print "\n", strings1, "\n",  strings2

	sameWords  =  compare(strings1,strings2) 

	print " the list of same words are: " , sameWords


# Boilerplate end of file stuff
if __name__ == '__main__':
  main()





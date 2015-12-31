#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

## CONTAINS functions
# def extract_names(filename):
# def sort_names(text):
# def print_to_screen(text):
# an added flag (not on commandline) for adding files to compare the first x names

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
 
"""
Given a file name for baby.html, returns a list starting with the year string
 followed by the name-rank strings in alphabetical order.
['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
 """


def extract_names(filename):
## first extract the year of the file	
	# open the file and start a dictionary 
	input_file = open(filename, 'r')
	count = 1
	names = {}

	# parse the file line by line
	# Extract the year in html file; store in variable the_year if exists	
	for line in input_file:
		year = re.search(r'(Popularity in)(\s)(\d\d\d\d)', line)
		if year: 
			the_year = year.group(3)
		
	##  extract both male and female names
	 # unpack the tuple, if boys/girls names not in dictionary names
	 # add the name= key, and its rank= value to dict. names
		names_by_rank = re.findall(r'<td>(\w+)</td><td>(\w+)</td><td>(\w+)', line)

		for name in names_by_rank:
			(rank, boys, girls) = name
			if boys not in names:
				names[boys] = rank
			if girls not in names:	
				names[girls] = rank
		
	# AFTER finished going through line by line, if no 	
	# match is found, exit the file and print out error message
	# I can't use if not year: here, but I can do an Exception handle
	# CHECK: if variable the_year, (the extracted year), exists
	try:
	 the_year
	except UnboundLocalError: 
		sys.stderr.write(" No year! Try another file \n")
		sys.exit(1)
		#return 2 things: all the names, and the current year!!
	return names,the_year
 

def sort_names(text):
	# this will print the names from the dictionary
	# make call to extract_names: unpack dict= names and var=year 
	# sort the dictionary into dict. names_ordered
	(names,year) = extract_names(text)	
	names_ordered = sorted(names.keys())
	final_list = []
	final_list.append(year)
	
  # print name, names[name]
  # create single string of name + rank and place into list. final_list
	for name in names_ordered:
		final_list.append(name + " " + names[name])
	return final_list

def print_to_screen(text):
	final_list = sort_names(text)
	print " ~~ the final_list for year " , final_list[0], " ~~ \n"	
	print " fist 10 names in final list " 
	for var in final_list[:10]:
		print var
	

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
	args = sys.argv[1:]

	if not args:
		print 'usage: [--summaryfile] file [file ...]'
		sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
	summary = False
	if args[0] == '--summaryfile':
		summary = True
		del args[0]
	
	# Parsing commandline arguments
	# args is a list that contains all the command line arguments
	# the last argument should be the filename	
	
	#BILLIE_edit: create a second file for comparison
	# do this only if -summaryfile is off; make no sense otherwise
	comparison = True

	if summary: 
		# call to extract_names, make the list text, with \n 
		filename = args[0]	
		(names,year) = extract_names(filename)
		names_sorted = sort_names(filename)

		text = '\n'.join(names_sorted)
		sumfile  = open(filename + '.summary', 'w')
		sumfile.write(text + '\n')
		sumfile.close()
		
	else:
		# first check if there's a second file for comparison
		# use an Exception Handle, because args[1] is empty -> index out of bounds
		while comparison:
			try: 
				file2 = args[1]
				break
			except IndexError: 
				print "please input a second file for comparison"
				sys.exit(1)
	
		filename = args[0] 
			# if flag --summaryfile given, file is second member in list	
			# if flag --summaryfile not given, file is first in list args
			# check if any other flags possible
		extract_names(filename)
		sort_names(filename)
		print_to_screen(filename)

	if comparison: 
		print "   ~~ Try another year for comparisoni ~~      "
		extract_names(file2)
		sort_names(file2)
		print_to_screen(file2)

  
if __name__ == '__main__':
  main()	

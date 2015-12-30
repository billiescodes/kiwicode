#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

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
	# open the file
	input_file = open(filename, 'r')
	count = 1
	# start a dictionary 
	names = {}
	
	for line in input_file:
	## Extract the year and print it 
		
		year = re.search(r'(Popularity in)(\s)(\d\d\d\d)', line)
			# note: do not need : * or + between parantheses to connect brackets ()
			# unless characters might repeat, like several spaces, then (\s*)m

		if year : 
			print year.group()
			#print " and the year is: ", year.group(3)
			the_year = year.group(3)
	##  extract both male and female names
		names_by_rank = re.findall(r'<td>(\w+)</td><td>(\w+)</td><td>(\w+)', line)

		for name in names_by_rank:
			#unpack the tuple
			(rank, boys, girls) = name
			# if boys name is not in dictionary:
			if boys not in names:
				names[boys] = rank
			if girls not in names:	
				names[girls] = rank
				# get every name, store as key and the rank as its value
			
		#return 2 things: all the names, and the current year!!
	return names,the_year

def sort_names(text):
	# this will print the names from the dictionary
	(names,year) = extract_names(text)			# make call to extract_names: names refers to dict
	names_ordered = sorted(names.keys())
	final_list = []
	final_list.append(year)
	print " ~~ the final_list is" , final_list, " ~~"
	for name in names_ordered:
	#	print name, names[name]
		# create a single string of name + rank and place into list
		final_list.append(name + " " + names[name])
	print " "
	print " fist 20 names of the list " 
	for var in final_list[:10]:
		print var



def Find(pat, text):
	match =  re.search(pat, text)
	if match: print match.group()
	#else:	print " match not found" 



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
	comparison = True
	
	if summary: 
		filename = args[1]	
		#	if not args[2]: 
		#	print "please input a second file for comparison" 
		#	sys.exit(1)
		#file2 = args[2]
	
	else:
		# first check if there's a second file for comparison
		# use an Exception Handle, because args[1] is empty -> index out of bounds
		while comparison:
			print "		~~ Try another year for comparisoni ~~			" 
			try: 
				file2 = args[1]
				break
			except IndexError: 
				print "please input a second file for comparison"
				sys.exit(1)

		#if not args[1]:
		#	sys.exit(1)
	
		filename = args[0] 
		#file2 = args[1]
			# if flag --summaryfile given, file is second member in list	
			# if flag --summaryfile not given, file is first in list args
			# check if any other flags possible
	extract_names(filename)
	sort_names(filename)
	if comparison: 
		extract_names(file2)
		sort_names(file2)


  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()	

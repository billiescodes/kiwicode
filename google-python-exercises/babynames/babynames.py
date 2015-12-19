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
	## as year consider 4 digits in a row	
	# open the file
	input_file = open(filename, 'r')
	count = 0
	
	for line in input_file:
		#year = re.search(r'(Popularity in)\s+(\d\d\d\d)', line)
		year = re.search(r'(Popularity in)(\s)(\d\d\d\d)', line)
			# note: do not need : * or + between parantheses to connect brackets ()
			# unless characters might repeat, like several spaces, then (\s*)m


		if year : 
			print year.group()
			print " and the year is: ", year.group(3)
	
	#match = re.search(r'(\s\s\s)(\d\d\d\d)', line)
	#if match : print match.group()
	print " search year  over"
	#Find('Michael', input_file) 
#	mymatch = re.findall(r'..<td>..',input_file)

#	for match in mymatch:
#		print match

	return


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
		
	if summary: filename = args[1]	
	else:	filename = args[0]
			# if flag --summaryfile given, file is second member in list	
			# if flag --summaryfile not given, file is first in list args
			# check if any other flags possible
	extract_names(filename)

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()	
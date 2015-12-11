#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):

# start an empty dictionary
  #sys.exit(0)
	dict = {}

# MASTERPLAN
# store word(i) as key and counter(i) into count1, as value
# go through text and perform the above for i through n words needed
# print 
	print "file is", filename.upper()
#open file
	f = open(filename, 'r') 
  #print every line
	count = 0
	size = 0
	for line in f:
		 
    # strategy: search for pattern in each line not sure how yet
	#	for key in dict:
	#		print "key is ", key

		if count == 222:
			print count, "*********line 222 is *********  ", size, line

      ### one way to loop through the words: get line and split along all whitespace
		## that's what no argument does
			nuline = line.split(' ')
			templen = len(nuline)
			nuline2 = [ ] 	
			a = 0

			#for a in range(2):
			for a in range(templen): 
				#nuline2[a] =
				#use append to add to nuline2, otherwise out of bound, i.e. above doesn't work
			 
				nuline2.append(nuline[a].translate(None, '`\',.:;'))
				print nuline2[a]
	
		## split along all commas
      #nuline2 = line.split(',')
		#	print nuline, "the split line and "
	#		print len(nuline), nuline[0],nuline[0].lstrip()
#			print " ***** nuline2 is *****" 
			
			#### I now have a way to break up all the words in every line of text
			print nuline2
			### now store in dictionary

			for a in range(templen):
				print "yo"	
				# if dictionary empty, just add a key
				if not dict: 
					dict[nuline2[a]] = 1
					print dict.items()

				for key in dict:
					print "hola"  
					if nuline2[a] == key: 
							# word is in dictionary, add another instance to counter
						dict[key] += 1
					else:
						# word is not in dictionary, so add as key dictionary
						dict[nuline2[a]] = 1
						print "here"

		count+=1
		#print dict.keys() 
					
#f.close()


#def print_top(filename):



###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

	# parsing commandline arguments right here: 
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print "filename is: ",  filename
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()

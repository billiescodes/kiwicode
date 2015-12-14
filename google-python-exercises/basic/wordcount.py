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
milestone and print your data strucuture and sys.exit(0).
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

def words_dict(filename):
	"""Creates a dictionary for all words, with counts """
# start an empty dictionary
	text = {}

	print "file is", filename.upper()
	input_file = open(filename, 'r')   # #open file 
	size = 0
	for line in input_file:
		 
    ### loop through the words: get line and split along all whitespace
		tmp_words = line.split()
		words = [ ] 	
		a = 0

		for a in range(len(tmp_words)): 
			# remove non-letter characters from split words
			words.append(tmp_words[a].translate(None, '-(")!?`\',.:;\n'))
			words[a] = words[a].lower()			# only consider lower-case
			
			### now store in dictionary
			# ~~special case~~ if dictionary EMPTY, just add a key
			if not text: 
				text[words[a]] = 1
			if words[a] in text.keys():
							# word is in dictionary, add another instance to counter
				text[words[a]] += 1
			else:
						# word is not in dictionary, so add as key to dictionary
				text[words[a]] = 1
			
	input_file.close() # close the file, return dictionary
	return text 

def print_words(filename):
	words = words_dict(filename)
	# now sort the keys in dictionary: 
	words_ordered = sorted(words.keys())
	#### loop through all words in words_ordered
	for word in words_ordered:
		print word, words[word]


def sortkey(tup):
	"""Returns the count from a dict word/count tuple  -- used for custom sort."""
	return tup[1]
 

def print_top(filename):
	#retrieve dictionary
	words = words_dict(filename)

	# the funciton returns column [1] of tuple --> sorts according to count 
	items = sorted(words.items(), key=sortkey, reverse=True)	

	## or use lambda function structure
	### That's two ways of doing it 
	items2 = sorted(words.items(), key=lambda tup:tup[1], reverse=True) 

	print " items: word -- count"
	#print the first 20 items
	for item in items2[:20]:					# this is the lambda version
		print item[0], " ",  item[1]
		


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

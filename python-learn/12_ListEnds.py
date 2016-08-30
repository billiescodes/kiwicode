#!/usr/bin/Python

#billiescodes 2016

#Write a program that takes a list of numbers 
#(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only 
# the first and last elements of the given list. For practice, write this code inside a function.

import random

def randgen(length):
	randlist = [ random.randint(1,100) for i in range(1,length)]
	return randlist
	
def ends(alist):
	nu=[]
	nu.append(alist[0])
	nu.append(alist[-1])
	return nu


def main():

	print "\n\t\t\t List Ends "
	a = [5, 10, 15, 20, 25]
	
	rand_a = randgen(20)	
	print "a-list is: " 
	print "endlist is: ", ends(a)
		
	print "random list \n ", rand_a
	print "endlist is: ", ends(rand_a)

# Boilerplate end of file stuff
if __name__ == '__main__':
  main()

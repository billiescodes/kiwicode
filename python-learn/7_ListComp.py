#!/usr/bin/Python

# billiescodes 2016
# Ex. 7. List comprehensions: 7_ListComp.py 
# given a list saved in a variable, a
# write IN ONE LINE: returns a new list with only EVEN elements of the list
import random

def randgen(length):
	randlist = [ random.randrange(1,10000) for a in range(length) ] 
	return randlist

def main():
 
	print "\n\t\t\t ~ List Comprehensions ~ "
	
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	print "list is: ", a
	nu_list = [ var for var in a if var%2==0 ] 
	print nu_list


	print "\n now generate random list (for practice) 100 elements" 
	b = randgen(100)
	print [ var for var in b if var%2==0] 

if __name__ =='__main__': 
	main()
